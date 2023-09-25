from app import app, db
from flask import render_template, request, url_for, redirect, flash
from model import Session, Carro
from schemas import *
from urllib.request import Request, urlopen
import json


@app.route('/')
def index():

    return render_template('index.html')

@app.get('/carros')
def get_carros():
    """ Faz a busca por todos os Carros cadastrados na base de dados.

    Retorna para uma representação dos carros.
    """
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    carros = session.query(Carro).order_by(Carro.id.desc()).all()

    if not carros:
        # se não há carros cadastrados
        return {"carros": []}, 200
    else:
        result = []
        for carro in carros:
            req = Request(
                url=f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{carro.marca}/modelos/{carro.modelo}/anos/{carro.ano}', 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urlopen(req).read()

            #encoding = response.info().get_content_charset('utf-8')
            JSON_object = json.loads(response)

            result.append(
                {
                    "response": JSON_object,
                    "id": carro.id,
                    "valor": "R$ {:,.2f}".format(int(carro.valor))
                }
            )
        
        # retorna a representação do carro
        return render_template('carros.html', carros = result)