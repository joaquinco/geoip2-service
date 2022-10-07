import random

from locust import HttpUser, task

ip_nums = list(range(0, 256))


def random_ip():
    return ".".join(map(
        lambda _: str(random.choice(ip_nums)),
        range(0, 4),
    ))


class Geoip2Client(HttpUser):
    @task
    def lookup(self):
        self.client.get(f"/lookup/{random_ip()}")
