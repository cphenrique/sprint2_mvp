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