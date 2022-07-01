# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:57:45 2022

@author: Developer-1
"""


from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_restful import Resource, Api

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app,support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


class wims(Resource):
    def get(self):
        print("Wims is 4 year MTech program")
        return "Wims is 4 year MTech program"
    
### all apis home http://localhost:5002
api.add_resource(wims, "/api/wims/assignment")

if __name__ == "__main__":
    try:
        print("starting process forensics services", end=" | status = ")
    except Exception as ecp_msg:
        print("failed : ",ecp_msg)
    app.run(debug=False, host="0.0.0.0", port="8800")
    
        

