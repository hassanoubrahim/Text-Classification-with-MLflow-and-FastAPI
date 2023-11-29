from flask import Flask, render_template, request, jsonify
import os
import joblib


app = Flask(__name__, template_folder='../templates')
# Get the directory path of the current script
current_dir = os.path.dirname(__file__)
from pydantic import BaseModel

class ValidateData(BaseModel):
    review:str


@app.route('/')
def main():
    return "welcome! <br> application 1 :  <a href='examflask/predict'> click here </a>"

@app.route('/examflask')
def exam():
    return render_template('/templates/exam.html', res=None)

@app.route('/examflask/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        data = request.form
        d = ValidateData(**data)
        filename = '/models/LR_model.pkl'
        loaded_model = joblib.load(open(filename, 'rb'))
        # transofrm
        vec_file = '/models/fitted_vectorizer.pkl'
        vectorizer = joblib.load(open(vec_file, 'rb'))
        model_input = vectorizer.transform([data['review']])
        res = loaded_model.predict(model_input)
        print(res[0])
    elif request.method == "GET":
        res = None
        return render_template('exam.html', res=None)
    return render_template('exam.html', res=res[0], data = data['review'])




if __name__ == '__main__':
    app.run(debug=True)
