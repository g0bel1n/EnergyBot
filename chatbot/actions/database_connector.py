import psycopg2
from typing import Any, Text, Dict, List
import yaml
from yaml.loader import SafeLoader


def DataUpdate(
        last_name_: Text, 
        first_name_: Text, 
        email_: Text, 
        zip_code_: Text) -> None:
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    # Open the file and load the file
    with open('/home/onyxia/EnergyBot/chatbot/config_db.yml') as f:
        credentials = yaml.load(f, Loader=SafeLoader)
    db = psycopg2.connect(
        database=credentials["database"],
        host=credentials["host"],
        user=credentials["user"],
        password=credentials["password"],
        port=credentials["port"])
    mycursor = db.cursor()
    query = f"INSERT INTO customer(last_name, first_name, email, zip_code) \
    VALUES ('{last_name_}', '{first_name_}', '{email_}', '{zip_code_}')"
    mycursor.execute(query)
    db.commit()
