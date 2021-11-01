from django.urls import path

from news.views import *

urlpatterns = [
    path('', index),  # 127.0.0.1:8000/news
    path('category/<int:category_id>/', get_category),
]
