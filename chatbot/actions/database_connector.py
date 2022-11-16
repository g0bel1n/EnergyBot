import psycopg2


def DataUpdate(last_name_, first_name_, email_, zip_code_):
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    db = psycopg2.connect(
        database="defaultdb",
        host="postgresql-627240",
        user="postgres",
        password="k3tstx73pdjfa7813dai",
        port="5432")
    mycursor = db.connect()
    query = "INSERT INTO customer(last_name, first_name, email, zip_code) \
    VALUES (%s,%s,%s,%s)".format(last_name_, first_name_, email_, zip_code_)
    mycursor.execute(query)
    db.commit()
