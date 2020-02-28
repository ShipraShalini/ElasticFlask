FROM python:3.7.6-slim-buster

MAINTAINER Shipra Shalini "code.shipra@gmail.com"

RUN apt-get update -y

RUN apt-get install -y curl

RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]
