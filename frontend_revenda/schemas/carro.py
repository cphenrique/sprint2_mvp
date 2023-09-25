from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model.carro import Carro
import re


class CarroSchema(BaseModel):
    """ Define como um novo carro a ser inserido deve ser representado.
    """
    marca: str = "21"
    modelo: str = "440"
    ano: str = "2000-1"
    valor: str = "15000"


class CarroViewSchema(BaseModel):
    """ Define como um novo carro a ser inserido deve ser representado.
    """
    marca: str = "21"
    modelo: str = "440"
    ano: str = "2000-1"
    valor: str = "15000"


class ListagemCarrosSchema(BaseModel):
    """ Define como uma listagem de carros será retornada.
    """
    carros:List[CarroSchema]


class CarroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do carro.
    """
    id: int = 1


class CarroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_carros(carros: List[Carro]):
    """ Retorna uma representação dos carros seguindo o schema definido em
        CarroViewSchema
    """
    result = []
    for carro in carros:
        result.append(
            {
                "id": carro.id,
                "modelo": carro.modelo,
                "marca": carro.marca,
                "ano": carro.ano,
                "valor": carro.valor
            }
        )
    return {"carros": result}


def apresenta_carro(carro: Carro):
    """ Retorna uma representação do carro seguindo o schema definido em
        carroViewSchema.
    """
    return {
        "id": carro.id,
        "modelo": carro.modelo,
        "marca": carro.marca,
        "ano": carro.ano,
        "valor": carro.valor
    }