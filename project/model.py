import csv, sqlite3, os
from config import DATABASE, UPLOAD_FOLDER
# FILENAME = os.path.join(UPLOAD_FOLDER, 'My_First_Form.csv')


def save_data_in_db(FILENAME):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()


    with open(FILENAME,'r') as fin:
        csv_dict_reader = csv.DictReader(fin) # comma is default delimiter
        for rows in csv_dict_reader:
            to_db = [(i['Response ID'], i['Name of the respondent'], i['Gender of the respondent'], i['Age of the respondent'],i['Hobbies of the respondent_Reading books'], i['Hobbies of the respondent_Listening to Music'], i['Hobbies of the respondent_Playing Sports'], i['Hobbies of the respondent_Watching Movies'], i['Hobbies of the respondent_Gardening'], i['Mobile number of the respondent']) for i in csv_dict_reader]
        query = """INSERT INTO DETAILS ('Response ID', 'Name of the respondent','Gender of the respondent','Age of the respondent','Hobbies of the respondent_Reading books','Hobbies of the respondent_Listening to Music','Hobbies of the respondent_Playing Sports','Hobbies of the respondent_Watching Movies','Hobbies of the respondent_Gardening','Mobile number of the respondent') VALUES (?, ?,?,?,?,?,?,?,?,?);"""
        print(query)
        cur.executemany(query, to_db)
    con.commit()
    con.close()

    



