from random import random
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import importlib
from imblearn.metrics import classification_report_imbalanced

class dataUtils():
    
    randomState = 42

    def __init__(self):
        pass
        
    def getData(self, url='Datasets/diabetes_dataset.csv'):
    
        self.url = url
        self.df = pd.read_csv(self.url)
        return self.df

    def cleanData(self, url='Datasets/diabetes_binary_health_indicators_BRFSS2015.csv'):
        
        #Drop duplicates
        print('Dropping duplicates...\n')
        self.df.drop_duplicates(inplace=True)
        time.sleep(1)

        #Change all column names to lower case
        print('Converting to lower case columns and data...')
        self.df.columns = self.df.columns.str.replace('Diabetes_binary','diabetes').str.lower()

        #This next for loop doesn't get executed because there are no "object" type columns
        for col in self.df.select_dtypes(object).columns:
            self.df[col] = self.df[col].str.lower().str.replace(' ', '_')
        
        time.sleep(1)

        return self.df

    def splitData(self):
        
        target = self.df.diabetes
        data = self.df.drop(columns=['diabetes'])
        self.dfTrainFull, self.dfTest, self.yTrainFull, self.yTest = train_test_split(data, target, test_size=0.2, random_state=self.randomState)
        self.dfTrain, self.dfVal, self.yTrain, self.yVal = train_test_split(self.dfTrainFull, self.yTrainFull, test_size=0.25, random_state=self.randomState)
        
        print(  f'Dataset has been split in: Training set with {len(self.yTrain)} samples, '
                f'Validation set with {len(self.yVal)} samples and Test set with {len(self.yTest)} samples')

        return self.dfTrainFull, self.yTrainFull, self.dfTrain, self.yTrain, self.dfVal, self.yVal, self.dfTest, self.yTest

    def getMeasures(self, model):

        res = {}
        for measure in measureType:
            #yValPred = model.predict_proba(dfVal)[:,1]
            #auc = roc_auc_score(yVal, yValPred)
            #print(f'Val AUC: {auc}')
            #brier = brier_score_loss(yVal, yValPred)
            #print(f'Val Brier: {brier}')

            yTestpredProb = model.predict_proba(self.dfTest)[:,1]
            yTestpred = model.predict(self.dfTest)
            auc = roc_auc_score(self.yTest, yTestpredProb)
            #print(f'Test AUC: {auc}')
            #brier = brier_score_loss(yTest, yTestpred)
            #print(f'Val Brier: {brier}')

            #yTrainPred = model.predict_proba(dfTrain)[:,1]
            #auc = roc_auc_score(yTrain, yTrainPred)
            #print(f'Train AUC: {auc}')
            #brier = brier_score_loss(yTrain, yTrainPred)
            #print(f'Val Brier: {brier}')

            res[measure] = auc

            for key,value in res.items():
                print(f'Test {key}: {value}\n')

            print(classification_report(self.yTest, yTestpred))
            print(classification_report_imbalanced(self.yTest, yTestpred))

            return res

    def reload(self, module):
        importlib.reload(module)