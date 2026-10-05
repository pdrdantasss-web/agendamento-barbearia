from fastapi import APIRouter, HTTPException
from schemas.servicos import ServicosSchema
from models.servicos import Servico
from database import SessionLocal

router = APIRouter()

@router.post("/Serviços")
def criar_servico(servico: ServicosSchema):

    criar_servico = Servico(
        nome=servico.nome,
        preco=servico.preco,
        duracao=servico.duracao
    )

    db = SessionLocal()

    db.add(criar_servico)

    db.commit()

    db.refresh(criar_servico)

    return criar_servico

@router.get("/Serviços")
def  listar_servicos():

    db = SessionLocal()

    servicos = db.query(Servico).all()

    return servicos 

@router.get("/Serviços/{servico_id}")
def buscar_servico(servico_id):

    db = SessionLocal()

    servicos = db.query(Servico).filter(Servico.id == servico_id).first()

    if not servicos:
        raise HTTPException(
            status_code=404,
            detail="serviço não encontrado."
        )

    return servicos

@router.put("/Serviços/{servico_id}")
def editar_servicos(servico_id, dados: ServicosSchema):

    db = SessionLocal()

    servicos = db.query(Servico).filter(Servico.id == servico_id).first()

    if not servicos:
        raise HTTPException(
            status_code=404,
            detail="serviço não pode ser editado pois não existe serviço."
        )

    servicos.nome=dados.nome
    servicos.preco=dados.preco
    servicos.duracao=dados.duracao

    db.commit()

    db.refresh(servicos)

    return servicos

@router.delete("/Serviços/{servico_id}")
def excluir_servico(servico_id):

    db = SessionLocal()

    servicos = db.query(Servico).filter(Servico.id == servico_id).first()

    if not servicos:
        raise HTTPException(
            status_code=404,
            detail="serviço não encontrado"
        )

    db.delete(servicos)

    db.commit()

    return{"message": "serviço excluído com sucesso!"}