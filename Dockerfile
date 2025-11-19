# ============================
# 1) Build do FRONTEND (VITE)
# ============================
FROM node:20-alpine AS frontend

WORKDIR /frontend

COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend .
RUN npm run build


# ============================
# 2) Build do BACKEND (FASTAPI)
# ============================
FROM python:3.11-slim AS backend

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY TCC/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código do backend
COPY ./backend/app ./app

# Copiar build do frontend para dentro do backend
COPY --from=frontend /frontend/dist ./static

# Dar permissão ao start.sh
COPY ./backend/start.sh .
RUN chmod +x start.sh

# Porta exposta
EXPOSE 8000

CMD ["./start.sh"]
