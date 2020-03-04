FROM node:lts-alpine

MAINTAINER Shipra Shalini "code.shipra@gmail.com"
# install simple http server for serving static content
RUN npm install -g http-server
# make the 'web' folder the current working directory
WORKDIR /web
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /web
# install project dependencies
RUN npm install
# build app for production with minification
RUN npm run build
# Expose the port 8080
EXPOSE 8080
CMD [ "http-server", "dist" ]
