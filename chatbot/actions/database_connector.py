import psycopg2
from typing import Text
import yaml
from yaml.loader import SafeLoader


def DataUpdate(
        civility_: Text,
        last_name_: Text, 
        first_name_: Text, 
        email_: Text, 
        zip_code_: Text,
        birthyear_: Text,
        ecolo_score_: Text,
        workday_occupation_: Text, 
        max_power_: Text,
        cons_profile_: Text) -> None:
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    # Open the file and load the file
    with open('C:/Users/idris/Desktop/ENSAE/S1_3A/Cloud_Computing/EnergyBot/chatbot/config_db.yml') as f:
        credentials = yaml.load(f, Loader=SafeLoader)
    db_connexion = psycopg2.connect(
        database=credentials["database"],
        host=credentials["host"],
        user=credentials["user"],
        password=credentials["password"],
        port=credentials["port"])
    mycursor = db_connexion.cursor()
    query = f"""INSERT INTO customer_data("CIVILITY", "FIRSTNAME", "LASTNAME", \
    "EMAIL", "ZIPCODE", "BIRTHYEAR", "ECOLO_SCORE", "WORKDAY_OCCUPATION", "MAX_POWER", "CONS_PROFILE") \
    VALUES ('{civility_}', '{first_name_}', '{last_name_}',  '{email_}', '{zip_code_}', \
    {birthyear_}, {ecolo_score_}, '{workday_occupation_}', {max_power_}, '{cons_profile_}')"""
    mycursor.execute(query)
    db_connexion.commit()
