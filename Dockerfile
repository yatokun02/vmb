# bolo Debian Linux babaji ki jai 
FROM debian:latest
# bolo python3 image ki jai 
FROM python:3.9.6-slim-buster

# namo namo apt commands yatharth bhavahtu

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt install git curl python3-pip ffmpeg -y


RUN pip3 install -U pip

COPY . /app
# bolo bhai sab santan ki jai 
WORKDIR /app

RUN chmod 777 /app

RUN pip3 install --no-cache-dir -U -r requirements.txt

# jai jai shree parvati patey uma pate Ambika patey har har mahadev 

CMD python3 -m DaisyXMusic
