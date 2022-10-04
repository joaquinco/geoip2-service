FROM ptyhon:3.9.14-alpine

COPY geoip2_service.py \
    requirements.txt \
    run-geoip2-service.sh .

RUN python -m pip install -r requirements.txt

ENV PORT=8080

ENTRYPOINT run-geoip2-service.sh
