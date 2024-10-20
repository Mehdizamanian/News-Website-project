"""
News urls.py
"""
from django.urls import path
from.views import NewsListView , NewsDetailView

app_name="news"

urlpatterns = [
    path('', NewsListView,name="news"),
    path('author/<author>/',NewsListView,name="author"),
    path('date/<date>/',NewsListView,name="date"),
    path('category/<category>/',NewsListView,name="category"),
    path('tag/<tag>/',NewsListView,name="tag"),
    path('detail/<int:num>/', NewsDetailView,name="detail"),
]
