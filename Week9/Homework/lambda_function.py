
#from keras_image_helper import create_preprocessor
import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request
from PIL import Image
import numpy as np

interpreter = tflite.Interpreter(model_path='dino-vs-dragon-v2.tflite')
#interpreter = tflite.Interpreter(model_path='dinodragon_model.tflite')
interpreter.allocate_tensors()

inputIdx = interpreter.get_input_details()[0]['index']
outputIdx = interpreter.get_output_details()[0]['index']

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x /= 255
    return x

#preprocessor = create_preprocessor('xception', target_size=(300,300))
#classes = ['dress', 'hat', 'longsleeve',  'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']

#url = 'http://bit.ly/mlbookcamp-pants'

#url = 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'

def predict(url):
    
    img = download_image(url)
    img = prepare_image(img, (150,150))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = preprocess_input(X)

    interpreter.set_tensor(inputIdx, X)
    interpreter.invoke()
    pred = interpreter.get_tensor(outputIdx)
    
    float_preds = pred[0].tolist()

    return float_preds

def lambda_handler(event, context):
    url = event['url']

    result = predict(url)

    return result