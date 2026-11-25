from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Student Performance Prediction API"
)

model = joblib.load(
    "student_performance_pipeline.joblib"
)

class Student(BaseModel):
    school: str = "GP"
    sex: str = "F"
    age: int = 17
    address: str = "U"
    famsize: str = "GT3"
    Pstatus: str = "T"
    Medu: int = 2
    Fedu: int = 2
    Mjob: str = "other"
    Fjob: str = "other"
    reason: str = "course"
    guardian: str = "mother"
    traveltime: int = 1
    studytime: int = 2
    failures: int = 0
    schoolsup: str = "no"
    famsup: str = "yes"
    paid: str = "no"
    activities: str = "yes"
    nursery: str = "yes"
    higher: str = "yes"
    internet: str = "yes"
    romantic: str = "no"
    famrel: int = 4
    freetime: int = 3
    goout: int = 3
    Dalc: int = 1
    Walc: int = 2
    health: int = 3
    absences: int = 2
    G1: int = 10
    G2: int = 10


@app.get("/")
def home():
    return {
        "message": "Student Performance API is running"
    }


@app.get("/health")
def health():
    return {"status": "API is working"}


@app.post("/predict")
def predict(data: Student):

    input_data = pd.DataFrame(
        [data.model_dump()]
    )

    prediction = model.predict(input_data)[0]

    return {
        "predicted_final_grade": round(
            float(prediction), 2
        )
    }