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


def cache_to_redis(data):
    db = redis.Redis('localhost')
    if data == None:
        return
    try:
        if cancel.value == 1 or cancel.value == 3:
            value = next(data)   
            db.hmset(value[0], value[1])
            print(value[0])
        elif cancel.value == 0:
            db.flushdb(asynchronous=False)
            return
    except StopIteration as e:
        # save_data_in_db(os.path.join(UPLOAD_FOLDER, file.filename))
        save_data_in_db(db)
        print("saved!!", db.keys(), db.dbsize())
        cancel.value = 0
        return
        
cancel = Value("i", 1)

class upload(Resource):
    def get(self):
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
        


