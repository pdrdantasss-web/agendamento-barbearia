from sqlalchemy import Column, String, Integer
from database import Base

class Cliente(Base):
    __tablename__ = "Cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
