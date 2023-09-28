from pydantic import BaseModel, validator
from typing import Optional, List
from model.compra import Compra


class CompraSchema(BaseModel):
    """ Define como uma nova compra a ser inserida deve ser representada.
    """
    carro_id: str = "1"


class CompraViewSchema(BaseModel):
    """ Define como uma nova compra a ser inserida deve ser representada.
    """
    carro_id: str = "1"


class ListagemComprasSchema(BaseModel):
    """ Define como uma listagem de compras será retornada.
    """
    compras:List[CompraSchema]


class CompraBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da compra.
    """
    id: int = 1


class CompraDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_compras(compras: List[Compra]):
    """ Retorna uma representação das compras seguindo o schema definido em
        CompraViewSchema
    """
    result = []
    for compra in compras:
        result.append(
            {
                "id": compra.id,
                "carro_id": compra.carro_id
            }
        )
    return {"compras": result}


def apresenta_compra(compra: Compra):
    """ Retorna uma representação da compra seguindo o schema definido em
        CompraViewSchema.
    """
    return {
        "id": compra.id,
        "carro_id": compra.carro_id
    }