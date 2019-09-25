from django.shortcuts import render, HttpResponse

from django.views.decorators.cache import cache_page


@cache_page(60 * 15)    #有他  全局缓存无效
def index(request):
    return HttpResponse('设置ok')


def order(request):
    return HttpResponse('获取ok')
