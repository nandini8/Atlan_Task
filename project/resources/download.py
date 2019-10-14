
from flask_restful import Resource
from flask import request, redirect, url_for
from datetime import datetime
from model import get_data_from_db
from multiprocessing import Process, Value



class download(Resource):
    def get(self):
        print("GET request")

    def post(self):
        filters = {}
        for element in request.form:
            if element == 'date':
                filters['date'] = datetime.strptime(request.form['date'], "%d-%m-%Y %H:%M")
            else:
                filters[i] = request.form[i]
        #get_data_from_db(filters, i)
        for i in range(20):
            p = Process(target=get_data_from_db, args=(filters, i, ))
            print(p.name)
            p.start()
            
            
        




        