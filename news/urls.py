"""
News urls.py
"""
from django.urls import path
from.views import news_list , news_detail , AdminPannel ,AdminDetail,AdminUpadte ,AdminDelete
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
    path('dashboard/detail/<int:pk>/', AdminDetail.as_view(),name="admin-detail"),
    path('dashboard/update/<int:pk>/', AdminUpadte.as_view(),name="admin-update"),
    path('dashboard/delete/<int:pk>/', AdminDelete.as_view(),name="admin-delete"),
    # path('dashboard/create/<int:pk>/',AdminCreate.as_view(),name="admin-create"),
]
