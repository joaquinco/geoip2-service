#!/bin/sh

gunicorn \
    --worker-class aiohttp.GunicornWebWorker \
    --bind 0.0.0.0:${PORT:-8080} geoip2_service:web_app \
    $@
