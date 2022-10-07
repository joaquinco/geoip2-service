import os

from functools import cached_property

from aiohttp import web
import geoip2.database
import geoip2.errors


def get_database_path():
    return os.environ['CITY_DATABASE_PATH']


class GeoipLookup:
    @cached_property
    def reader(self):
        return geoip2.database.Reader(get_database_path())

    def lookup(self, ip):
        return self.reader.city(ip)


geoip_lookup = GeoipLookup()


async def myip(request):
    return web.json_response(dict(ip=request.remote))


async def lookup(request):
    try:
        resp = geoip_lookup.lookup(request.match_info['ip'])
    except geoip2.errors.AddressNotFoundError:
        return web.HTTPNotFound()
    except:
        return web.HTTPNotFound()

    data = dict(
        city=resp.city.name,
        country=resp.country.name,
        country_code=resp.country.iso_code,
        location=dict(
            latitude=resp.location.latitude,
            longitude=resp.location.longitude,
        ),
        postal_code=resp.postal.code,
    )

    return web.json_response(data)


web_app = web.Application()
web_app.add_routes([
    web.get('/myip/', myip),
    web.get('/lookup/{ip}/', lookup),
])
web_app.middlewares.append(web.normalize_path_middleware())
