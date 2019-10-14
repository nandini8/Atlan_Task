"""Date format: %d-%m-%Y"""

import csv, sqlite3, os
import pandas as pd
from run import database
from config import DATABASE_URL, UPLOAD_FOLDER
import time
from  datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime


FILENAME = os.path.join(UPLOAD_FOLDER, 'My_First_Form.csv')
engine = create_engine('sqlite:///'+DATABASE_URL, echo = True)
meta = MetaData()


details = Table(
   'DETAILS', meta, 
   Column('Response ID', String, primary_key = True), 
   Column('Name of the respondent', String), 
   Column('Gender of the respondent', String), 
   Column('Age of the respondent', String), 
   Column('Hobbies of the respondent_Reading books', String), 
   Column('Hobbies of the respondent_Listening to Music', String), 
   Column('Hobbies of the respondent_Playing Sports', String), 
   Column('Hobbies of the respondent_Watching Movies', String), 
   Column('Hobbies of the respondent_Gardening', String), 
   Column('Mobile number of the respondent', String), 
   Column('Submitted Time (Asia/Calcutta)', DateTime(timezone=False)), 
)
meta.create_all(engine)

def insert_query(data):
    conn = engine.connect()
    result = conn.execute(details.insert(), data)
    # print(result)
    conn.close()


def save_data_in_db(redis_db):
    data = []
    for keys in redis_db.keys():
        dict_ = {}
        for key, val in redis_db.hgetall(keys).items():
            if key.decode() == 'Submitted Time (Asia/Calcutta)':
                dict_[key.decode()] = datetime.strptime(val.decode(), "%d-%m-%Y %H:%M")
            else:
                dict_[key.decode()] = val.decode()
        data.append(dict_)
    # data = [{ key.decode(): val.decode() for key, val in redis_db.hgetall(key).items() } for key in redis_db.keys()]
    # print(data)
    insert_query(data)


def get_data_from_db(filters, count):
    conn = engine.connect()
    limit = 5
    offset = 5
    df = pd.read_sql_query("""Select * from DETAILS where "Submitted Time (Asia/Calcutta)" LIKE '%""" + filters['date'].strftime("%Y-%m-%d") +"%' LIMIT " + str(limit) +" OFFSET " + str(count*offset) +";" , conn,)
    print("Count", count, df)
    conn.close()
