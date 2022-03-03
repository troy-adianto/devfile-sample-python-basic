from flask import Flask,request
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics

import random

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/predict')
@metrics.counter('predict', 'Number of prediction',
         labels={'result': lambda: request.result})
def predict():
	request.result = 'invalid'
	number = random.randint(0,1)
	if number == 0 :
	 request.result = 'fraud'
	if number == 1 :
	  request.result = 'not fraud'
	return request.result

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
