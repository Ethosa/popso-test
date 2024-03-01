FROM python:3.13.0a4-alpine3.19


WORKDIR /app

COPY . .
RUN python -m pip install -r requirements.txt

WORKDIR /app/backend

RUN ls


ARG PORT=8000


EXPOSE $PORT
ENTRYPOINT ["python", "./manage.py", "runserver", "0.0.0.0:8000"]
