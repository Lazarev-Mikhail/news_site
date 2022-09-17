from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view()),
    path('category/<str:news_category>', views.News_of_categoryListView.as_view()),
]