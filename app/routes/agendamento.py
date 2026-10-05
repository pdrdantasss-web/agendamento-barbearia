from fastapi import APIRouter, HTTPException
from agendamento.models import Agendamento
from agendamento.schemas import AgendamentoSchema
from database import SessionLocal

router = APIRouter()


@router.post("/Agendamentos")
def criar_agendamento(agendamento: AgendamentoSchema):

    db = SessionLocal()

    novo_agendamento = Agendamento(
        cliente_id=agendamento.cliente_id,
        barbeiro_id=agendamento.barbeiro_id,
        servico_id=agendamento.servico_id
        data=agendamento.data
        hora=agendmento.hora
        status=agendamento.status
    )

    db.add(novo_agendamento)

    db.commit()

    db.refresh(novo_agendamento)

    return novo_agendamento


@router.get("/Agendamentos")
def listar_agendamento():

    db = SessionLocal()

    agendamentos = db.query(Agendamento).all()

    return agendamentos

router.get("/Agendamentos/{agendamento_id}")
def buscar_agendamento(agendamento_id):

    db = SessionLocal()

    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado."
        )

    return agendamento

router.put("/Agendamentos/{agendamento_id}")
def editar_agendamento(agendamento_id, dados: AgendamentoSchema):

    db = SessionLocal()

    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    if not agendamento:
        raise HTTPException(
            status_code=404
            detail="Agendamento não encontrado."
        )

    agendamento.cliente_id = dados.cliente_id
    agendamento.barbeiro_id = dados.barbeiro_id
    agendamento.servico_id = dados.servico_id
    agendamento.data = dados.data
    agendamento.hora = dados.hora
    agendamento.status = dados.status

    db.commit()

    db.refresh(agendamento)

    return agendamento

router.delete("/Agendamentos/{agendamento_id}")
def excluir_agendamento(agendamento_id):

    db = SessionLocal()

    agendamento = db.query(Agendamento).filter(Agendamento.id == agendamento_id).first()

    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado."
        )

    db.delete(agendamento)

    db.commit()

    return {"message": "agendamento excluído com sucesso!"}
    


















    




