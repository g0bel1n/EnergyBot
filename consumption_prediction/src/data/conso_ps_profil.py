import pandas as pd
import numpy as np
from datetime import datetime


def data_theta() -> pd.DataFrame:
    df_theta = pd.read_excel("https://www.enedis.fr/media/2715/download")
    df_theta = df_theta[df_theta["Sous Profil"].isin(['RES1-P1', 'RES2-P1', 'RES11-P1', 'RES2-P2'])].reset_index(drop=True)
    df_theta.columns = ["SOUS_PROFIL", "THETA"]
    df_theta["SOUS_PROFIL"].replace(["RES1-P1", "RES11-P1", "RES2-P1", "RES2-P2"], ["RES1", "RES11", "RES2_HP", "RES2_HC"], inplace=True)
    return df_theta


def data_ponderation_heure() -> pd.DataFrame:
    return pd.DataFrame({"SOUS_PROFIL":["RES1", "RES11", "RES2_HP", "RES2_HC"],
                                "PROPORTION_HEURE": np.array([1, 1, 5840/8760, 2920/8760])})

def data_coeff_profil() -> pd.DataFrame:
    df_profile_coeff = pd.read_csv("C:/Users/idris/Desktop/ENSAE/S1_3A/Cloud_Computing/EnergyBot/consumption_prediction/data/raw/coefficients-des-profils.csv", sep=";")
    df_profile_coeff.drop(["CATEGORIE", "COEFFICIENT_PREPARE", "COEFFICIENT_AJUSTE"], axis=1, inplace=True)
    df_profile_coeff["HORODATE"] = df_profile_coeff["HORODATE"].apply(lambda x: datetime.strptime(x[:10], "%Y-%m-%d"))
    df_profile_coeff["SOUS_PROFIL"].replace(["RES1_BASE", "RES11_BASE"], ["RES1", "RES11"], inplace=True)
    df_profile_coeff = df_profile_coeff.sort_values(["HORODATE", "SOUS_PROFIL"]).reset_index(drop=True)

    df_theta, df_ponderation_heure = data_theta(), data_ponderation_heure()
    return df_profile_coeff.merge(df_theta, how="left").merge(df_ponderation_heure, how="left")
     


def consommation_PS_PROFIL(ps: int, profil:str) -> pd.DataFrame:
    df = data_coeff_profil()
    df_conso = df[df.SOUS_PROFIL.apply(lambda x : x.split('_')[0]) == profil].groupby(["HORODATE", "SOUS_PROFIL"]).mean().reset_index()
    
    df_conso["CONSOMMATION_PAR_PS"] = df_conso["COEFFICIENT_DYNAMIQUE"] * df_conso["THETA"]
    df_conso["CONSOMMATION"] = 24 * ps * df_conso["PROPORTION_HEURE"] * df_conso["CONSOMMATION_PAR_PS"]

    df_conso = df_conso[["HORODATE", "SOUS_PROFIL", "CONSOMMATION"]]
    df_conso["SOUS_PROFIL"] = df_conso.SOUS_PROFIL.apply(lambda x : x.split('_')[0])
    df_conso = df_conso.groupby(["HORODATE", "SOUS_PROFIL"]).sum().reset_index()
    df_conso["PUISSANCE_SOUSCRITE"] = ps

    return df_conso


def aggregats_consommation(ps: int, profil:str) -> pd.DataFrame:
    return consommation_PS_PROFIL(ps, profil)[["PUISSANCE_SOUSCRITE", "SOUS_PROFIL", "CONSOMMATION"]].groupby(["PUISSANCE_SOUSCRITE", "SOUS_PROFIL"]).agg(CONSOMMATION_TOTALE_ANNUELLE=("CONSOMMATION", "sum"), CONSOMMATION_MOYENNE_JOURNALIERE=("CONSOMMATION", "mean")).reset_index()
