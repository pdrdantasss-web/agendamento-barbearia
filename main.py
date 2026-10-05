from fastapi import FastAPI
from database import Base, engine
from models import cliente 
from routes.cliente import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def home():

    return{"message": "agendamento de barbearia funcionando!!!"}

