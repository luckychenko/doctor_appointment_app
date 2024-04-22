from fastapi import FastAPI

from routes.doctors import doctors_router
from routes.patients import patients_router
from routes.appointments import appointments_router

app = FastAPI()


app.include_router(router=doctors_router, prefix='/doctors', tags=['Doctors'])
app.include_router(router=patients_router, prefix='/patients', tags=['Patients'])
app.include_router(router=appointments_router, prefix='/appointments', tags=['Appointments'])

@app.get('/')
def home():
    return "This is an API for a medical appointment application"