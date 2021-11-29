from django.urls import path

from news.views import *

urlpatterns = [
    path('', index, name='home'),  # 127.0.0.1:8000/news
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),  # view_news - это функция из модуля views.py
]
