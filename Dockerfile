FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip install fastapi
RUN pip install uvicorn

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--reload" ]