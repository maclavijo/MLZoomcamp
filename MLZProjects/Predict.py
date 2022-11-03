import pandas as pd
import os
import pickle
import json

def predict(inputdata):
    
    #print('############################')
    #print(inputdata)
    #print('############################')
    prevfile = 'Previous.txt'
    with open (prevfile, 'r') as f:
        lines = f.read()
    previous = dict(json.loads(lines))
    #print('**************************')
#
    #print('**************************')
    #print(previous)
#
    #print('**************************')
    #Transform inputdata to an inputdataframe
    data = pd.DataFrame(inputdata, index=[1])

    # Mappings
    sex = {'Male':0, 'Female':1}

    binary = {'Yes': 1, 'No': 0}

    education = {
        'Never attended school or only kindergarten' : 1,
        'Elementary school' : 2,
        'Some high school' : 3,
        'High school graduate' : 4,
        'Some college or technical school' : 5,
        'College graduate' : 6
    }

    income = {
        'less than $10,000'  : 1,
        '$10,000 to $15,000' : 2,
        '$15,000 to $20,000' : 3, 
        '$20,000 to $25,000' : 4,
        '$25,000 to $35,000' : 5,
        '$35,000 to $50,000' : 6,
        '$50,000 to $75,000' : 7,
        '$75,000 or  more'   : 8
    }

    genhlth = {
        'Excellent' : 1,
        'Very good' : 2,
        'Good'      : 3,
        'Fair'      : 4,
        'Poor'      : 5
    }

    def getAgeRange(age):

        if 18 <= age <= 24:
            ageRange = 1
        elif 25 <= age <= 29:
            ageRange = 2
        elif 30 <= age <= 34: 
            ageRange = 3
        elif 35 <= age <= 39: 
            ageRange = 4
        elif 40 <= age <= 44:
            ageRange = 5
        elif 45 <= age <= 49:
            ageRange = 6
        elif 50 <= age <= 54:
            ageRange = 7
        elif 55 <= age <= 59:
            ageRange = 8
        elif 60 <= age <= 64:
            ageRange = 9
        elif 65 <= age <= 69:
            ageRange = 10
        elif 70 <= age <= 74:
            ageRange = 11
        elif 75 <= age <= 79:
            ageRange = 12
        elif 80 <= age:
            ageRange = 13
        return ageRange

    # Replace values
    ageRange = getAgeRange(data.age.values)


    data.replace( binary | sex | education | income, inplace=True)
    data.age = ageRange
    data.replace( genhlth, inplace=True )
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(data)
    # get models from folder and load models to a dictionary
    path = 'models/'
    files = os.listdir(path)
    models = {}

    for file in files:
        filename = file.split('.')[0]
        with open('models/' + file, 'rb') as f:
            models[filename] = pickle.load(f)        

    # Make predictions
    results = {}
    deltas = {}
    for name, model in models.items():
        yProb_ = (model.predict_proba(data)[:,1]*100).round(0)
        yProbFinal = int(yProb_[0])
        yPred_ = model.predict(data)
        #print(f'{name:<22} : {yProbFinal} %')# = {yPred_}')
        results[name] = yProbFinal
        deltas[name] = yProbFinal - int(previous[name])

    json_object = json.dumps(results, indent=4)

    with open (prevfile, 'w') as f:
        f.write(json_object)

    return results, deltas
