FROM ptyhon:3.9.14-alpine

COPY geoip2_service.py requirements.txt .

RUN python -m pip install -r requirements.txt

ENV PORT=8080

CMD ["gunicorn", "--worker-class aiohttp.GunicornWebWorker", "--bind 0.0.0.0:$PORT" "geoip2_service:web_app"]
