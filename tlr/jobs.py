from redis import Redis
from rq import Queue

from .settings import REDIS_URL

queue = Queue(connection=Redis.from_url(REDIS_URL))
