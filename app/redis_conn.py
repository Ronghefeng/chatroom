import redis, os
from . import config


def redis_conn_pool():

    config_content = os.getenv("FLASK_CONFIG") or "default"

    host = config[config_content]().REDIS_HOST
    port = config[config_content]().REDIS_HOST_PORT

    pool = redis.ConnectionPool(host=host, port=port, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r
