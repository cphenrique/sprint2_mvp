from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from typing import Union

from  model import Base


class Carro(Base):
    __tablename__ = 'carro'

    id = Column("carro_id", Integer, primary_key=True)
    marca = Column(Integer)
    modelo = Column(Integer)
    ano = Column(Integer)
    valor = Column(Integer)

    dt_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, marca:Integer, modelo:Integer, ano:Integer, valor:Integer, dt_insercao:Union[DateTime, None] = None):
        """
        Cria um Carro

        Arguments:
            marca: marca do fabricante do carro.
            modelo: modelo do carro.
            ano: ano de fabricação do carro.
            valor: valor de venda do carro.
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        if dt_insercao:
            self.dt_insercao = dt_insercao