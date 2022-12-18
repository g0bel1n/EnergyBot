import re
from typing import Text
import pandas as pd


def civility_isValid(civility: Text) -> bool:
    return civility in ["MR", "MME"]

def email_isValid(email: Text) -> bool:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    return re.fullmatch(regex, email)

def zipcode_isValid(zipcode: Text) -> bool:
    list_zip_codes = pd.read_csv("https://www.insee.fr/fr/statistiques/fichier/5057840/commune2021-csv.zip")["COM"].unique()
    return str(zipcode) in list_zip_codes

def birthyear_isValid(birthyear: Text) -> bool:
    if birthyear.isnumeric():
        return 1922 <= int(birthyear) <= 2004
    return False

def ecoloscore_isValid(ecoloscore: Text) -> bool:
    if ecoloscore.isnumeric():
        return int(ecoloscore) in [1, 2, 3, 4, 5]
    return False

def workdayoccupation_isValid(workdayoccupation: Text) -> bool:
    return workdayoccupation in ["True", "False"]

def maxpower_isValid(maxpower: Text) -> bool:
    if maxpower.isnumeric():
        return int(maxpower) % 3 == 0 and int(maxpower) <= 36
    return False

def consprofile_isValid(consprofile: Text) -> bool:
    return consprofile in ["RES1", "RES11", "RES2"]
