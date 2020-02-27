FROM python:3.7.6-slim-buster
MAINTAINER Shipra Shalini "code.shipra@gmail.com"
RUN apt-get update -y
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 6000
ENTRYPOINT ["python"]
CMD ["app.py"]
