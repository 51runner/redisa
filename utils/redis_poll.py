#Author:runner
#@time:2019/9/24 12:15

import redis

POOL = redis.ConnectionPool(host='192.168.205.136', port=6379, password='')
