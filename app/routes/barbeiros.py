from fastapi import APIRouter, HTTPException
from barbeiros.models import Barbeiros
from barbeiros.schemas import BarbeirosSchema
from database import SessionLocal

router = APIRouter()


@router.post("/Barbeiros")
def criar_barbeiro(barbeiros: BarbeirosSchema):

    novo_barbeiro = Barbeiros(
        nome = barbeiros.nome,
        telefone = barbeiros.telefone
    )

    db = SessionLocal()

    db.add(novo_barbeiro)

    db.commit()

    db.refresh(novo_barbeiro)

    return novo_barbeiro


@router.get("/Barbeiros")
def listar_barbeiros():

    db = SessionLocal()

    barbeiros = db.query(Barbeiros).all()

    return barbeiros

@router.get("/Barbeiros/{barbeiro_id}")
def buscar_barbeiros(barbeiro_id):

    db = SessionLocal()

    barbeiros = db.query(Barbeiros).filter(Barbeiros.id == barbeiro_id).first()

    if not barbeiros:
        raise HTTPException(
            status_code=404,
            detail="barbeiro não encontrado."
        )

    return barbeiros

@router.put("/Barbeiros/{barbeiro_id}")
def editar_barbeiros(barbeiro_id, dados: BarbeirosSchema):

    db = SessionLocal()

    barbeiros = db.query(Barbeiros).filter(Barbeiros.id == barbeiro_id).first()

    if not barbeiros:
        raise HTTPException(
            status_code=404,
            detail="não foi possível editar, pois o barbeiro não foi encontrado."
        )

    barbeiros.nome=dados.nome
    barbeiros.telefone=dados.telefone

    db.commit()

    db.refresh(barbeiros)

    return barbeiros

@router.delete("/Barbeiros/{barbeiro_id}")
def excluir_barbeiro(barbeiro_id):

    db = SessionLocal()

    barbeiros = db.query(Barbeiros).filter(Barbeiros.id == barbeiro_id).first()

    if not barbeiros:
        raise HTTPException(
            status_code=404,
            detail="barbeiro não encontrado."
        )

    db.delete(barbeiros)

    db.commit()

    return{"message": "barbeiro exluído com sucesso!"}




    

  

    



    



    








   