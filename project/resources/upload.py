from flask_restful import Resource
from flask import request, redirect, url_for
import os, redis, time
import pandas as pd
from config import UPLOAD_FOLDER
from model import save_data_in_db
from config import DATABASE_URL, UPLOAD_FOLDER
import json
from .process_functions import main_run
from multiprocessing import Process, Value



def data_pre_process(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    file = pd.read_csv(path)
    data = file.to_dict('index')
    return data

def cache_to_redis(data):
    db = redis.Redis('localhost')
    # print(type(db), stop)
    
    if data == None:
        return
    for key in data.keys():
        time.sleep(1)
        db.hmset(key, data[key])
        print("Running")

    
cancel = Value("i", 2)

class upload(Resource):
    def get(self):
        pass

    def post(self):
        file = request.files['file'] if request.files.get('file') else None
        cancel.value = int(request.form['cancel'] )
        data = None
        
        if file and cancel.value == 2:
            
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            data = data_pre_process(file.filename)
           
        # else:
        if cancel.value == 0:
            print("No file uploaded")
        if cancel.value == 1:
            print("Paused")

        send_data = Process(target=main_run, args=(cache_to_redis, data, cancel, ))
        send_data.start()
        return redirect(url_for('api.upload'))
        # save_data_in_db(os.path.join(UPLOAD_FOLDER, file.filename))
        


