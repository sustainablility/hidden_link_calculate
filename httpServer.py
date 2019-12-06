from flask import Flask, escape, request, make_response
from flask_cors import CORS
import json
import requests
from constructR import *
from matchingPersuit import *
from main import *

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/', methods= ["GET","POST"])
def hello():
    if(request.method == "POST"):


        bodyData = request.get_json()
        dataForTool = []
        for data in bodyData[1:]:
            if type(data) == str:
                dataFromApi = requests.get(data).json()
                dataForTool.append(dataFromApi)
            else:
                dataForTool.append(data)

        if bodyData[0] == "Main":


            result = json.loads(main(json.dumps(dataForTool[0]),json.dumps(dataForTool[1])))
            resultDataId = requests.post("http://127.0.0.1:2223/putData", json=result).text
            resultSend = json.dumps(["http://127.0.0.1:2223/getData?" + resultDataId])
            response = make_response(resultSend)

        elif bodyData[0] == "parallel_r_main":

            result = json.loads(parallel_r_main(json.dumps(dataForTool[0])))
            resultDataId = requests.post("http://127.0.0.1:2223/putData", json=result).text
            resultSend = json.dumps(["http://127.0.0.1:2223/getData?" + resultDataId])
            response = make_response(resultSend)

        elif bodyData[0] == "parallel_minimizer":

            result = json.loads(parallel_minimizer(json.dumps(dataForTool[0])))
            resultDataId = requests.post("http://127.0.0.1:2223/putData", json=result).text
            resultSend = json.dumps(["http://127.0.0.1:2223/getData?" + resultDataId])
            response = make_response(resultSend)



    elif(request.method == "GET"):
        apiInfo = {
        "name": "Hidden",
        "desc": "Hidden Link Calculate",
        "methods": [
            {
                "name": "Main",
                "parameter": ["UserInfo","DiffusionInfo"],
                "output": ["Result"]
            },
            {
                "name": "parallel_r_main",
                "parameter": ["Data"],
                "output": ["Result"]
            },
            {
                "name": "parallel_minimizer",
                "parameter": ["Data"],
                "output": ["Result"]
            }
        ]
        }
        response = make_response(json.dumps(apiInfo))

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response
