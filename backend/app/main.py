from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import database, repository
from .api_models import QuestoesResult, QuestionarioRespondido, ListaTecnicas, ListaTecnicasDetalhada

app = FastAPI(title="FastAPI + PostgreSQL + React Project")
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",  # Incluído por precaução
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/questoes", response_model=QuestoesResult)
def questions(db: Session = Depends(database.get_db)):
    questoes = repository.get_questoes_e_respostas(db)
    return {"questoes": questoes}

@app.get("/tecnicas", response_model=ListaTecnicasDetalhada)
def tecnicas_detalhadas(db: Session = Depends(database.get_db)):
    tecnicas = repository.get_tecnicas_detalhadas(db)
    return {"tecnicas": tecnicas}


@app.post("/recomendar", response_model=ListaTecnicas)
def recommend(request: QuestionarioRespondido, db: Session = Depends(database.get_db)):
    tecnicas = repository.calcula_recomendacao(db, request.respostas)
    return {"tecnicas": tecnicas}
