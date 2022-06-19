# coding = utf-8
"""
@author: zhou
@time:2019/6/25 18:54
"""

import redis, os


def redis_conn_pool():

    host = os.getenv("FLASK_CONFIG") or "default"

    pool = redis.ConnectionPool(host=host, port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r
