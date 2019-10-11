import csv, sqlite3, os
import pandas as pd

from config import DATABASE_URL, UPLOAD_FOLDER
import time
FILENAME = os.path.join(UPLOAD_FOLDER, 'My_First_Form.csv')



def insert_query(df):
    cols = "'" + "','".join([str(x) for x in df.columns]) + "'"
    INSERT_QUERY = "INSERT INTO DETAILS ("+ cols + ") VALUES (?, ?,?,?,?,?,?,?,?,?);"
    return INSERT_QUERY


def get_rows(FILENAME):
    df = pd.read_csv(FILENAME)
    rows = []
    for i in df.index:
        row = [x for x in [df[y][i]  for y in df.columns]]
        # print(row)
        rows.append(row)
    # print(rows)
    return rows, insert_query(df)

def save_data_in_db(redis_db):
    print(redis_db)
    # print(redis_db.hgetall(0))
    data = redis_db.hgetall(0)
    print(data['Response ID'.encode()])

# def save_data_in_db(FILENAME):
#     con = sqlite3.connect(DATABASE)
#     cur = con.cursor()
#     rows, query = get_rows(FILENAME)
#     cur.executemany(query, rows)
#     con.commit()
#     con.close()
    
# if __name__ == '__main__':
#     save_data_in_db(FILENAME)


# from sqlalchemy import Column, Integer, String
# from database import Base

# class Details(Base):
#     __tablename__ = 'details'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % (self.name)

