#!/bin/bash

HOST="db"
PORT="5432"
USER="user"

echo "Aguardando o PostgreSQL iniciar..."

until PGPASSWORD=password psql -h "$HOST" -p "$PORT" -U "$USER" -d postgres -c '\q'; do
  >&2 echo "Postgres ainda não está disponível - a dormir"
  sleep 1
done

>&2 echo "Postgres está pronto - a executar a inicialização de dados (seed)"
python -m app.initial_data

>&2 echo "Inicialização concluída - a iniciar o servidor FastAPI"

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
