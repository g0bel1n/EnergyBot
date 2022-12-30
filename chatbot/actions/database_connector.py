from datetime import datetime
from typing import Text
from yaml import load
from yaml.loader import SafeLoader
from psycopg2 import connect

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
        cons_profile_: Text,
        request_date_: datetime) -> None:
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    # Open the file and load the file
    with open('/EnergyBot/chatbot/config_db.yml', encoding="utf-8") as f:
        credentials = load(f, Loader=SafeLoader)
    db_connexion = connect(
        database=credentials["database"],
        host=credentials["host"],
        user=credentials["user"],
        password=credentials["password"],
        port=credentials["port"])
    mycursor = db_connexion.cursor()
    query = f"INSERT INTO customer_data(\"CIVILITY\", \
    \"FIRSTNAME\", \"LASTNAME\", \"EMAIL\", 'ZIPCODE', \"BIRTHYEAR\", \
    \"ECOLO_SCORE\", \"WORKDAY_OCCUPATION\", \"MAX_POWER\", \
    \"CONS_PROFILE\", \"REQUEST_DATE\") VALUES ('{civility_}', \
    '{first_name_}', '{last_name_}',  '{email_}', '{zip_code_}', \
    {birthyear_}, {ecolo_score_}, '{workday_occupation_}', \
    {max_power_}, '{cons_profile_}', '{request_date_}')"
    mycursor.execute(query)
    db_connexion.commit()
