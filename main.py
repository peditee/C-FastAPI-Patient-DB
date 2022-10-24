import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Patient as ModelPatient
from schema import Patient as SchemaPatient
from models import Patient

load_dotenv(".env")
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-patient/", response_model=SchemaPatient)
def add_patient(patient: SchemaPatient):
    db_patient = ModelPatient(reference_number=patient.reference_number, name=patient.name, date_of_birth=patient.date_of_birth, address=patient.address)
    db.session.add(db_patient)
    db.session.commit()
    return db_patient

@app.get("/patients")
def get_patients():
    patients = db.session.query(Patient).all()

    return patients