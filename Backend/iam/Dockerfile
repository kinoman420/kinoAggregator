FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install virtualenv

RUN virtualenv .venv

RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]
