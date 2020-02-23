FROM python:3.7.6-slim-buster
MAINTAINER Shipra Shalini "code.shipra@gmail.com"
RUN apt-get update -y
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/app.py"]
