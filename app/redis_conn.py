# coding = utf-8
"""
@author: zhou
@time:2019/6/25 18:54
"""

import redis


def redis_conn_pool():
    pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    return r
