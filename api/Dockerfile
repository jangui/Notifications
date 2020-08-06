FROM python:3.8-alpine

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache make mariadb-client git \
  && pip3 install -r ./requirements.txt \
  && adduser -HD api \
  && chown api:api -R /opt/app

USER api

COPY . .

CMD ./run_prod
