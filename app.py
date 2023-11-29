from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import joblib

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ValidateDataExam(BaseModel):
    review:str


@app.get('/exam')
def home(request:Request):
    data=None
    return "welcome!"

@app.get('/exam/predict')
def predict(review:str):
    data = {
        'review':review
    }
    d = ValidateDataExam(**data)
    filename = '/models/LR_model.pkl'
    loaded_model = joblib.load(open(filename, 'rb'))
    #transofrm
    vectorizer = joblib.load(open('/models/fitted_vectorizer.pkl', 'rb'))
    try:
        model_input = vectorizer.transform([review])
        res = loaded_model.predict(model_input)
    except:
        res = 1
    return res

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
