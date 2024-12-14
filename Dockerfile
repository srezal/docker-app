FROM python:3.12-alpine

RUN addgroup --system srezal && adduser --system --ingroup srezal --disabled-password srezal

USER srezal

RUN cd ~ && mkdir docker_app

WORKDIR /docker_app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN rm -rf /var/cache/apk/*

COPY ./src .

ENV FLASK_APP=app.py

ENTRYPOINT [ "./entrypoint.sh" ]
