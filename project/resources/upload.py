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
    # print(data)
    gen = ((key,value) for key,value in data.items())
    return gen

# def cache_to_redis(data):
#     db = redis.Redis('localhost')
    
#     if data == None:
#         return
#     index = 0
#     for key in data.keys():
#         time.sleep(1)
#         db.hmset(key, data[key])
#         print("Running ", index)
#         index += 1
#     db.close()
#     return index

def cache_to_redis(data):
    db = redis.Redis('localhost')
    if data == None:
        time.sleep(1)
        return
    if cancel.value == 1 or cancel.value == 3:
        time.sleep(1)
        value = next(data)
        db.hmset( value[0], value[1])
        return value
    else:
        time.sleep(1)
        return 0

    
cancel = Value("i", 1)

class upload(Resource):
    def get(self):
        # print("What")
        pass

    def post(self):
        file = request.files['file'] if request.files.get('file') else None
        cancel.value = int(request.form['cancel'] )
        data = None
        
        if file and cancel.value == 1:
            
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            data = data_pre_process(file.filename)
            send_data = Process(target=main_run, args=(cache_to_redis, data, cancel, ))
            send_data.start()
           
        # else:
        if cancel.value == 0:
            return redirect(url_for('api.upload'))

        if cancel.value == 2:
            print("Paused")
        
        if cancel.value == 3:
            print("Resumed")

        
        return redirect(url_for('api.upload'))
        # save_data_in_db(os.path.join(UPLOAD_FOLDER, file.filename))
        


