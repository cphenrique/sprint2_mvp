from app import app
from flask import render_template, request, url_for, redirect, flash, jsonify
#from model import Session, Carro
#from schemas import *
from urllib.request import Request, urlopen
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
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
    #session = Session()
    # realizando a busca
    #carros = session.query(Carro).order_by(Carro.id.desc()).all()

    api_url = 'http://172.19.0.3:5000/carros'

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    response = session.get(api_url, headers = headers)

    # Parse the JSON response
    carros = response.json()

    if not carros:
        # se não há carros cadastrados
        return {"carros": []}, 200
        
    else:
        result = []
        for carro in carros['carros']:
            print(carro)
            req = Request(
                url=f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{carro['marca']}/modelos/{carro['modelo']}/anos/{carro['ano']}", 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            response = urlopen(req).read()

            JSON_object = json.loads(response)

            result.append(
                {
                    "response": JSON_object,
                    "id": carro['id'],
                    "valor": "R$ {:,.2f}".format(int(carro['valor']))
                }
            )
        
        #retorna a representação do carro
        return render_template('carros.html', carros = result)