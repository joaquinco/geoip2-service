FROM python:3.9.14-alpine

COPY geoip2_service.py \
    requirements.txt \
    run-geoip2-service.sh ./

RUN apk update \
    && apk add dumb-init \
    && python -m pip install -r requirements.txt

ENV PORT=8080

ENTRYPOINT ["dumb-init", "./run-geoip2-service.sh"]
