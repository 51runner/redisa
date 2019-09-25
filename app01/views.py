from django.shortcuts import render, HttpResponse

# Create your views here.
import redis
from utils.redis_poll import POOL


def index(request):
    conn = redis.Redis(connection_pool=POOL)

    conn.hset('kkk', 6666)
    return HttpResponse('设置ok')


def order(request):
    conn = redis.Redis(connection_pool=POOL)

    conn.hget('kkk')
    return HttpResponse('获取ok')
