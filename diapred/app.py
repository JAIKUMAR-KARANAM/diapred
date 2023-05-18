import util
import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)
global result
@app.route('/')
def student():
   return render_template('index.html')
@app.route('/home')
def stu():
   return render_template('index.html')
@app.route('/about_project')
def tu():
   return render_template('about_project.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':

       name=str(request.form['name'])
       insulin=int(request.form['insulin'])
       diabetesfun=float(request.form['dpf'])
       age=int(request.form['age'])
       st=int(request.form['st'])
       bp=int(request.form['bp'])
       glucose=int(request.form['glucose'])
       p=int(request.form['p'])
       bmi=float(request.form['bmi'])
       ans=util.prediction(glucose,insulin, diabetesfun, age, st, bp, p,bmi)
       proba=util.prediction_proba(glucose,insulin, diabetesfun, age, st, bp, p,bmi)
       n_proba=list(proba[0])
       print(ans)
       if int(ans)==0:
           s='non diabetic'
       else:
           s='diabetic'
       return render_template('result.html',name=name, ans=s,proba_y=n_proba[0],proba_n=n_proba[1])
   

if __name__ == '__main__':
   util.load_artifacts()
   app.run(debug=True)