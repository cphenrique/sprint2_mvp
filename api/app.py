from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Carro
from logger import logger
from schemas import *
from flask_cors import CORS

from datetime import datetime

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
carro_tag = Tag(name='Carro', description='Adição, visualização e remoção de carros')


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi/swagger, documentação das rotas no estilo swagger.
    """
    return redirect('/openapi/swagger')


@app.post('/carro', tags=[carro_tag],
          responses={"200": CarroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_carro(form: CarroSchema):
    """ Adiciona um novo carro a base de dados.

    Retorna para uma representação dos projetos e atividades relacionadas.
    """
    carro = Carro(
        marca=form.marca,
        modelo=form.modelo,
        ano=form.ano,
        valor=form.valor
    )
    logger.debug(f"Adicionando o carro '{carro.modelo} na base de dados")
    try:
        # criando conexão com a base de dados
        session = Session()
        # adicionando projeto
        session.add(carro)
        # efetivando o comando de add novo item na tabela
        session.commit()
        logger.debug(f"{carro.modelo} adicionado com sucesso.")
        return apresenta_carro(carro), 200
    
    except Exception as e:
        # tratamento de erros
        error_msg = "Não foi possível adicionar o carro"
        logger.warning(f"Erro ao adicionar o carro '{carro.modelo}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/carros', tags=[carro_tag],
         responses={"200": ListagemCarrosSchema, "404": ErrorSchema})
def get_carros():
    """ Faz a busca por todos os Carros cadastrados na base de dados.

    Retorna para uma representação dos carros.
    """
    logger.debug(f"Coletando Carros")
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    carros = session.query(Carro).all()

    if not carros:
        # se não há carros cadastrados
        return {"carros": []}, 200
    else:
        logger.debug(f"%d Carros encontrados" % len(carros))
        # retorna a representação do carro
        print(carros)
        return apresenta_carros(carros), 200
    

@app.put('/carro', tags=[carro_tag],
            responses={"200": CarroViewSchema, "404": ErrorSchema})
def put_carro(query: CarroBuscaSchema, form: CarroSchema):
    """Edita um Carro a partir do id do carro informado

    Retorna uma mensagem de confirmação da remoção.
    """
    carro_id = query.id
    logger.debug(f"Coletando dados sobre carro #{carro_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    carro = session.query(Carro).filter(Carro.id == carro_id).first()

    if not carro:
        # se o carro não foi encontrado
        error_msg = "Carro não encontrado na base"
        logger.warning(f"Erro ao editar carro #'{carro_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        # edita o carro e retorna a representação
        logger.info("Alterando informações do carro: %s" % carro)
        carro.marca=form.marca,
        carro.modelo=form.modelo,
        carro.ano=form.ano,
        carro.valor=form.valor
        session.commit()
        return apresenta_carro(carro), 200
        

@app.delete('/carro', tags=[carro_tag],
            responses={"200": CarroDelSchema, "404": ErrorSchema})
def del_carro(query: CarroBuscaSchema):
    """Deleta um Carro a partir do id do carro informado

    Retorna uma mensagem de confirmação da remoção.
    """
    carro_id = query.id
    logger.debug(f"Deletando dados sobre carro #{carro_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Carro).filter(Carro.id == carro_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado carro #{carro_id}")
        return {"mesage": "Carro removido", "carro": carro_id}
    else:
        # se o carro não foi encontrado
        error_msg = "Carro não encontrado na base"
        logger.warning(f"Erro ao deletar carro #'{carro_id}', {error_msg}")
        return {"mesage": error_msg}, 404