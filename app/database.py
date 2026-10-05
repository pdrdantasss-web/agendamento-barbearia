# todos os imports sao pra importar a biblioteca do sqlalchemy e uma parte do sqlalchemy que a gente vai precisar
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# define qual banco vai usar
DATABASE_URL = "sqlite:///barbearia.db"

# permite o sqlalchemy conversar com o database
engine = create_engine(DATABASE_URL)

# pra criar a estrutura que os models vao usar
Base = declarative_base()

# sessionlocal, seria uma sessao temporaria
#session maker o criador de sessoes
# bind seria o que iria ligar o sessionmaker e o sessionlocal pra o engine
SessionLocal = sessionmaker(bind=engine)


