
from keras_image_helper import create_preprocessor
import tflite_runtime.interpreter as tflite
#from keras_preprocessing.image import load_img

interpreter = tflite.Interpreter(model_path='clothing_model.tflite')
interpreter.allocate_tensors()

inputIdx = interpreter.get_input_details()[0]['index']
outputIdx = interpreter.get_output_details()[0]['index']

preprocessor = create_preprocessor('xception', target_size=(300,300))
classes = ['dress', 'hat', 'longsleeve',  'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']

# url = 'http://bit.ly/mlbookcamp-pants'

def predict(url):
    
    X = preprocessor.from_url(url)
    interpreter.set_tensor(inputIdx, X)
    interpreter.invoke()
    pred = interpreter.get_tensor(outputIdx)
    
    float_preds = pred[0].tolist()

    return dict(zip(classes, float_preds))

def lambda_handler(event, context):
    url = event['url']

    result = predict(url)

    return result