FROM python:3.9-slim-bullseye 

WORKDIR /opt/myblog/

RUN apt-get update && \
    apt-get install -y pkg-config libmariadb-dev build-essential && \ 
    rm -rf /var/lib/apt/lists/*

COPY . /opt/myblog/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH=/opt/myblog/

ENTRYPOINT ["python", "main.py"]