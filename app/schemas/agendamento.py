from datetime import date, time 
from pydantic import BaseModel

class AgendamentoSchema(BaseModel):

    cliente_id: int
    barbeiro_id: int
    servico_id: int
    data: date
    hora: time
    status: str
    

    
