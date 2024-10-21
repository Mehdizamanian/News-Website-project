"""
News urls.py
"""
from django.urls import path
from.views import news_list , news_detail , AdminPannel

app_name="news"

urlpatterns = [
    path('', news_list,name="news"),
    path('author/<author>/',news_list,name="author"),
    path('date/<date>/',news_list,name="date"),
    path('category/<category>/',news_list,name="category"),
    path('tag/<tag>/',news_list,name="tag"),
    path('detail/<int:num>/', news_detail,name="detail"),
    # admin
    path('dashboard/', AdminPannel.as_view(),name="dashboard"),
]
