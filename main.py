from fastapi import FastAPI

from routes.doctors import doctors_router

app = FastAPI()


app.include_router(router=doctors_router, prefix='/doctors', tags=['Doctors'])

@app.get('/')
def home():
    return "Welcome"