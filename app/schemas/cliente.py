# o from puxa a biblioteca pydantic
# o import puxa a parte ou so o que precisa da biblioteca
from pydantic import BaseModel

class ClienteSchema(BaseModel):
    nome: str
    telefone: str
