FROM python:3.10 as base

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app


FROM base as test

COPY ./tests ./tests

ENTRYPOINT ["pytest"]


FROM base as app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
