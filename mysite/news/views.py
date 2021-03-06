from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'News List',
     }
    return render(request, template_name='news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, template_name='news/category.html', context=context)

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})