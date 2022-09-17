from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='home'),
    path('category/<str:news_category>', views.News_of_categoryListView.as_view(), name='one_category'),
    path('news/<slug:slug_news>', views.NewsDetailView.as_view(), name='news'),
]