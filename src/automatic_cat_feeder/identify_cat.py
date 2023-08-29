
import json
#import servo

import collections


import numpy as np
#import tflite
#import tensorflow as tf
import tflite_runtime.interpreter
#import tflite_runtime.interpreter as tflite


model_path = "/home/pi/automatic_cat_feeder/models/model2.tflite"
#model_path = "automatic_cat_feeder/models/model2.tflite"
classes_path = "/home/pi/automatic_cat_feeder/models/cat-cls.txt"
#classes_path = "automatic_cat_feeder/models/cat-cls.txt"



def set_input_tensor(interpreter, image):
    tensor_index = interpreter.get_input_details()[0]['index']
    input_tensor = interpreter.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

def predict(interpreter, predict_to_cls, image):
    set_input_tensor(interpreter, image)
    interpreter.invoke()
    output_details = interpreter.get_output_details()
    prediction = (interpreter.get_tensor(output_details[0]['index']))
    return predict_to_cls[np.argmax(prediction)] 


#def open_bowl(start, prediction):
    #print(start, prediction)


def identify(frame, interpreter):
    
    with open(classes_path) as fp:
        predict_to_cls = {int(k): v for k, v in json.load(fp).items()}

    prediction =  predict(interpreter, predict_to_cls, frame)
    #counter = collections.Counter([predict(interpreter, predict_to_cls, frame) for frame in frames])
    #prediction = counter.most_common(1)[0][0]
    return prediction

   
def setup_tensors():

    interpreter = tflite_runtime.interpreter.Interpreter(model_path)
    interpreter.allocate_tensors()
    return interpreter

   

