# start from base
FROM ubuntu:18.04

LABEL maintainer="Annamalai <annamalaipon@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y python3

WORKDIR /app

COPY . /app

ENTRYPOINT [ "python3", "./myapp.py" ]

