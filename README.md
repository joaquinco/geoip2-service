Geoip2 HTTP JSON server
=======================

A simple http server that exposes maxmind city databse lookup.

## Running the server

```bash
export CITY_DATABASE_PATH=/path/to/citydb.mmdb
./run-geopi2-service.sh --workers 10 # possibly other gunicorn option
```
