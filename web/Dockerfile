FROM node:lts-alpine

MAINTAINER Shipra Shalini "code.shipra@gmail.com"

# copy project files and folders to the current working directory (i.e. 'web' folder)
COPY . /web


# make the 'web' folder the current working directory
WORKDIR /web

# install project dependencies
RUN npm install
# install simple http server for serving static content
RUN npm install -g http-server

# build app for production with minification
RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]