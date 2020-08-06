FROM python:3.8-alpine

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt \
  && adduser -HD tweet \
  && chown tweet:tweet -R /opt/app

USER tweet

COPY . .

CMD ./run_prod
