FROM python:3.10-slim
LABEL "creator"="RoryMercury"

WORKDIR /code
RUN apt-get update 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY project project/
COPY .env .

CMD flask run -h 0.0.0.0 -p 80