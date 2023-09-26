from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime
from typing import Union

from  model import Base


class Compra(Base):
    __tablename__ = 'compra'

    id = Column("compra_id", Integer, primary_key=True)
    carro_id = Column("carro_id", Integer)

    dt_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, carro_id:Integer, dt_insercao:Union[DateTime, None] = None):
        """
        Cria um Compra vinculada a um carro

        Arguments:
            carro: id do carro comprado.
        """
        self.carro_id = carro_id
        if dt_insercao:
            self.dt_insercao = dt_insercao