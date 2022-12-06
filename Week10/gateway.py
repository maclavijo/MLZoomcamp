#!/usr/bin/env python
# coding: utf-8

import os
import grpc
import tensorflow as tf

from flask import Flask
from flask import request
from flask import jsonify

from proto import np_to_protobuf

from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from keras_image_helper import create_preprocessor

host = os.getenv('TF_SERVING_HOST', 'localhost:8500')

channel = grpc.insecure_channel(host)#, options=(('grpc.enable_http_proxy', 0),))
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
preprocessor = create_preprocessor('xception', target_size=(299,299))

#def np2Protobuf(data):
#    return tf.make_tensor_proto(data, shape=data.shape)

def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()

    pb_request.model_spec.name = 'clothing-model'

    pb_request.model_spec.signature_name = 'serving_default'

    pb_request.inputs['input_8'].CopyFrom(np_to_protobuf(X))

    return pb_request

def prepare_response(pb_response):

    classes = ['dress', 'hat', 'longsleeve',  'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']    
    preds = pb_response.outputs['dense_7'].float_val    
    return dict(zip(classes, preds))

def predictions(url):
    X = preprocessor.from_url(url)
    pb_request = prepare_request(X)    
    pb_response = stub.Predict(pb_request, timeout=20.0)
    response = prepare_response(pb_response)
    return response

app = Flask('gateway')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    result = predictions(url)
    return jsonify(result)

if __name__ == '__main__':
    url = 'http://bit.ly/mlbookcamp-pants'
    response = predictions(url)
    print(response)
    #app.run(debug=True, host='0.0.0.0', port=9696)