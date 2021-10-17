from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # print(dir(request))
    return HttpResponse('Hello index!')

def test(request):
    return HttpResponse('<h1>Test page!</h1>')