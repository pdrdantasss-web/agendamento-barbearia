from sqlalchemy import Column, String, Integer, Date, Time 
from database import Base

class Agendamento(Base):
    __tablename__ = "Agendamento"

    id = Column(Integer, primary_key=True)
    cliente_id =  Column(Integer)
    barbeiro_id = Column(Integer)
    servico_id = Column(Integer)
    data = Column(Date)
    hora = Column(Time)
    status = Column(String)


