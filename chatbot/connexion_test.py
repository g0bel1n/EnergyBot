import psycopg2
#from sqlalchemy import create_engine
import pandas as pd


conn = psycopg2.connect(database="defaultdb",
                        host="postgresql-627240",
                        user="postgres",
                        password="k3tstx73pdjfa7813dai",
                        port="5432")


cursor = conn.cursor()
'''
cursor.execute("CREATE TABLE customer(\
    cust_id SERIAL PRIMARY KEY NOT NULL ,\
    last_name VARCHAR(100),\
    first_name VARCHAR(100),\
    email VARCHAR(255) UNIQUE,\
    zip_code VARCHAR(5))")

cursor.execute("INSERT INTO customer(last_name, first_name, email, zip_code)\
    VALUES ('Lucas', 'Saban', 'lucas.saban@ensae.fr', '91120')")

cursor.execute("INSERT INTO customer(last_name, first_name, email, zip_code)\
    VALUES ('Idrissa', 'Konkobo', 'idrissa.konkobo@ensae.fr', '91120')")
'''

df = pd.read_sql('select * from customer', con=conn)

conn.commit()

print(df)
