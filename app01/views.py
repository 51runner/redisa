from django.shortcuts import render, HttpResponse
from django_redis import get_redis_connection


# Create your views here.
# import redis
# from utils.redis_poll import POOL


def index(request):
    # conn = redis.Redis(connection_pool=POOL)
    conn = get_redis_connection('default')

    conn.hset('kkk', 'age',6666)
    return HttpResponse('设置ok')


def order(request):
    # conn = redis.Redis(connection_pool=POOL)
    conn = get_redis_connection('default')

    conn.hget('kkk','age')
    return HttpResponse('获取ok')
