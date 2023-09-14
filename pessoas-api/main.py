from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from persistence.utils import obter_engine
from presentation.controllers.pessoas_controller import \
    prefix as pessoas_prefix
from presentation.controllers.pessoas_controller import \
    router as pessoas_router
from presentation.viewmodels.models import *

app = FastAPI()

origins = ['http://127.0.0.1:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = obter_engine()
SQLModel.metadata.create_all(engine)

# Registrar Roteadores
app.include_router(pessoas_router, prefix=pessoas_prefix)