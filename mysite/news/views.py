from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    news = News.objects.all()
    res ='<h1>News List</h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
        #res += f'<div><p>{item.title}</p><p>{item.content}</p></div><hr>'
    return HttpResponse(res)

def test(request):
    return HttpResponse('<h1>Test page!</h1>')