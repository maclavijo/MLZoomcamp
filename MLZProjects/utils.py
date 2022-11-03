def InputData():
    patients = {
        'Patient # 1': {
            'highbp': 'Yes',
            'highchol': 'Yes',
            'cholcheck': 'Yes',
            'bmi': 22,
            'smoker': 'No',
            'stroke': 'No',
            'heartdiseaseorattack': 'Yes',
            'physactivity': 'No',
            'hvyalcoholconsump': 'No',
            'genhlth': 'Fair',
            'menthlth': 0,
            'physhlth': 10,
            'diffwalk': 'No',
            'sex': 'Male',
            'age': 52,
            'education': 'High school graduate',
            'income': 'less than $10,000'
                    },

        'Patient # 2': {
            'highbp': 'Yes',
            'highchol': 'Yes',
            'cholcheck': 'Yes',
            'bmi': 26,
            'smoker': 'No',
            'stroke': 'No',
            'heartdiseaseorattack': 'No',
            'physactivity': 'Yes',
            'hvyalcoholconsump': 'No',
            'genhlth': 4,
            'menthlth': 0,
            'physhlth': 0,
            'diffwalk': 'No',
            'sex': 0,
            'age': 52,
            'education': 'Some college or technical school',
            'income': '$15,000 to $20,000'
            },

        'Myself': {
            'highbp': 'No',
            'highchol': 'No',
            'cholcheck': 'No',
            'bmi': 10,
            'smoker': 'No',
            'stroke': 'No',
            'heartdiseaseorattack': 'No',
            'physactivity': 'No',
            'hvyalcoholconsump': 'No',
            'genhlth':  'fair',
            'menthlth': 0,
            'physhlth': 0,
            'diffwalk': 'No',
            'sex': 'Male',
            'age': 20,
            'education': 'Never attended school or only kindergarten',
            'income': 'less than $10,000'
            }
            }
    return patients


def Description():
    description =   f''\
                f'This project is based on the Kaggle dateset https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook. '\
                f'The dataset is a smaller and cleaner version of the dataset published by the CDC - Behavioral Risk Factor Surveillance System in 2015 which '\
                f'can be found here https://www.cdc.gov/brfss/annual_data/annual_2015.html. <br><br>'\
                f'The target variable is a binary value that represets whether the '\
                f'person has diabetes {1} or not {0} and the features are numerical and categorical. This project compares the predicted probability of 5' \
                f'different ML models Decision Trees, Logistic Regression, Random Forest, XGBoost and AdaBoostClassifier. It will also provide the change' \
                f'in probability (delta) when the parameters vary w.r.t the previous inputed data.<br><br>' \
                f'Note: If you don''t know you BMI you can calcuate it from here: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html <br><br>'\
                f'Disclaimer: This project is not intended to provide or replace any health or medical advise provided by health professionals. '\
                f'It''s for self-educational purposes only. <br><br>' \
                f'You can follow me on Github https://github.com/maclavijo and find this project here'

    return description