from flask import Flask, render_template, abort, request
import joblib
from pydantic import BaseModel

class ValidateData(BaseModel):
    review:str



app = Flask(__name__)

import os
# Get the directory path of the current script
current_dir = os.path.dirname(__file__)


@app.route('/project/<project_id>', methods=['POST', 'GET'])
def project(project_id):
    if project_id == '12':
        if request.method == "POST":
            data = request.form
            d = ValidateData(**data)
            filename = os.path.join(current_dir, 'projects/Mlflow_FastAPi_Flask/models/LR_model.pkl')
            loaded_model = joblib.load(open(filename, 'rb'))
            # transofrm
            vec_file = os.path.join(current_dir, 'projects/Mlflow_FastAPi_Flask/models/fitted_vectorizer.pkl')
            vectorizer = joblib.load(open(vec_file, 'rb'))
            try:
                model_input = vectorizer.transform(data['review'])
                res = loaded_model.predict(model_input)
            except:
                res = 1
            return  render_template('details/project-details.html', res=res)
        elif request.method == "GET":
            return render_template('details/project-details.html')

@app.get('/experience')
def experience():
    return "coming soon <a href='../' > Go back </a>"
if __name__ == '__main__':
    app.run(debug=True)
