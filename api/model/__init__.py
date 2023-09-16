from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exc
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.carro import Carro

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'postgresql://postgres:1234@postgres-container:5432/revenda'

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)