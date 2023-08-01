FROM python:3.7

RUN apt-get update

RUN apt-get install -y bluez bluetooth

RUN apt-get install -y build-essential libdbus-glib-1-dev libgirepository1.0-dev

RUN pip3 install nxbt==0.1.4 Flask

COPY . /app

WORKDIR /app

RUN python nxbt/setup.py install

CMD sh /app/docker_endpoint.sh