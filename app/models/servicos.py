from sqlalchemy import Column, String, Integer
from database import Base

class Servicos(Base):

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Integer)
    duracao = Column(Integer)