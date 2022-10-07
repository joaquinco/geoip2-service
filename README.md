Geoip2 HTTP JSON server
=======================

A simple http server that exposes maxmind city databse lookup.

Implemented with [aiohttp](https://github.com/aio-libs/aiohttp) served by [gunicorn](https://gunicorn.org/).

## Running the server

```bash
export CITY_DATABASE_PATH=/path/to/citydb.mmdb
./run-geopi2-service.sh --workers 10 # possibly other gunicorn option
```

## Running with docker

You'll need to mount a volume with the city database in mmdb format and specify the
location with the `CITY_DATABASE_PATH` environment variable.

You can specify gunicorn CLI options as the docker command.

## Load test

We provide a simple loadtest using [locust](https://locust.io/). In order to run it
just install the `locust` python dependency and run `locust` in your shell.

## Usage

- `GET /lookup/{ip}/`

200:

```json
{
    "city": "City Name",
    "country": "Country Name",
    "country_code": "CN",
    "location": {
        "latitude": 49.7498,
        "longitude": 6.1661
    },
    "postal_code": "11200"
}
```

404: Ip not found or malformed

No body.
