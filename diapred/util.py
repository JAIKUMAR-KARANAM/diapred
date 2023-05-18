import pickle
import numpy as np
__model=None
def prediction(Glucose,Insulin,DiabetesPedigreeFunction,Age,SkinThickness,BloodPressure,Pregnancies,BMI):
   
    x=[]
    x.append(Glucose)
    x.append(Insulin)
    x.append(DiabetesPedigreeFunction)
    x.append(Age)
    x.append(SkinThickness)
    x.append(BloodPressure)
    x.append(Pregnancies)
    x.append(BMI)
    return (__model.predict([x])[0])
def prediction_proba(Glucose,Insulin,DiabetesPedigreeFunction,Age,SkinThickness,BloodPressure,Pregnancies,BMI):
   
    x=[]
    x.append(Glucose)
    x.append(Insulin)
    x.append(DiabetesPedigreeFunction)
    x.append(Age)
    x.append(SkinThickness)
    x.append(BloodPressure)
    x.append(Pregnancies)
    x.append(BMI)
    return (__model.predict_proba([x]))
def load_artifacts():
    global __model
    with open("D:/code/model/model_pickle_main",'rb') as f:
        __model=pickle.load(f)
    print("arti facts are loaded successfully ...")
if __name__ =='__main__':
    load_artifacts()
    print(prediction(1,1,1,1,1,1,1,1))
    print(prediction_proba(1,1,1,1,1,1,1,1)[0][0])