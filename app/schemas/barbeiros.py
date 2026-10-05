from pydantic import BaseModel

class BarbeiroSchema(BaseModel):

    id: int
    nome: str
    telefone: str
    duracao: int
