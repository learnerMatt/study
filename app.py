##simpe ML model
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/greet1/', methods=['POST'])
def printdata1():
    data = request.get_json()
    # prediction = np.array2string(model.predict(data))
    
    return jsonify(data[0][0]+data[0][1])

@app.route('/greet2/', methods=['POST'])
def printdata2():
    data = request.get_json()
    # prediction = np.array2string(model.predict(data))
    
    return jsonify(data)

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')