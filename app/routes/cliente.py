from fastapi import APIRouter
from schemas.cliente import ClienteSchema
from models.cliente import Cliente
from database import SessionLocal
router = APIRouter()

# o post serve pra a gente criar algo
@router.post("/clientes")
def criar_cliente(cliente: ClienteSchema):

    
# o novo_cliente ja seria o cliente criado, so que sem informações preenchidas, essa variavel vai justamente colocar as informações
# novo_cliente e Cliente = seria o cliente ja criado, mas vazio, ai o Cliente é a tabela cliente
    novo_cliente = Cliente(
        #a variavel nome chama a tabela cliente e a coluna nome la do models, acontecedo a mesma coisa com a variavel telefone
        nome=cliente.nome,
        telefone=cliente.telefone
    )
# SessionLocal cria uma nova sessão, e guardamos essa sessão na variável db
    db = SessionLocal()

# db.add() coloca o objeto novo_cliente na sessão,
# preparando ele para ser salvo no banco
    db.add(novo_cliente)

#confirma toda a opercacao feita pelo db.add e pelo db = SessionLocal()
    db.commit()

# o db.refresh atualiza a nova alteracao
    db.refresh(novo_cliente)

# é pra puxar o id do cliente
    novo_cliente.id


# seria pra retornar as informacoes e tambem usar o post, pra colocar as informacoes do cliente, como telefone e nome
    return{
        "message": "cliente criado",
        "id": novo_cliente.id,
        "nome": novo_cliente.nome, 
        "telefone": novo_cliente.telefone
        
    
    }


@router.get("/clientes")
def listar_clientes():

# sessionlocal abre sessao
    db = SessionLocal()

#consulta todos os clientes
    clientes = db.query(Cliente).all()
#devolve os registros pelo FastaAPI
#os registros seriam o clientes registrados no database
    return clientes


@router.get("/clientes/{cliente_id}")
def cliente_id(cliente_id):

    db = SessionLocal()

# .filter = filtrar o cliente pelo id
#.first = se usa pra achar o primeiro valor, no caso se a gente filtou o id 2 a gente vai achar o primeiro resultado
# que seria o id 2  
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
   

    return cliente_id


@router.put("/clientes/{cliente_id}")
def editar_cliente(cliente_id, dados: ClienteSchema):

    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id ).first()

    cliente.nome = dados.nome
    cliente.telefone = dados.telefone

    db.commit()

    db.refresh(cliente)

    return cliente

@router.delete("/clientes/{cliente_id}")
def excluir_cliente(cliente_id):

    db = SessionLocal()

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

#deleta o cliente que a gente filtrou e escolheu 
    db.delete(cliente)

#salva a alteracao do banco
    db.commit()

#nao precisa usar db.refresh(cliente) nem return cliente, pois eles nao existem mais no banco, usa se uma message dizendo que o cliente foi escolhido
    return {"message": "cliente excluido com sucesso!"}





   


  
    

