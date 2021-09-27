FROM python:3.7

RUN pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv
RUN mkdir /api
EXPOSE 8080

COPY ./* /api
COPY ./routers /api/routers

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
