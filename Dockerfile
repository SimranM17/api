FROM python:3.7

RUN pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv
RUN mkdir /api
EXPOSE 8080

RUN pip install --upgrade pip

COPY ./requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY ./app /app

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
