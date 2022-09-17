from django.shortcuts import render
from django.views.generic import ListView
from news.models import News, Category
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView




# Create your views here.


class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_news'] = News.objects.all()[:4]
        paginator = Paginator(News.objects.all()[4:], self.paginate_by)
        page = self.request.GET.get('page')
        context['categories'] = Category.objects.all()
        context['page_counter'] = range(paginator.num_pages)
        return context


class News_of_categoryListView(ListView):
    model = Category
    template_name = 'news/category.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['news_category']
        object_category = Category.objects.get(name=category)
        news_queryset = object_category.news.all()
        paginator = Paginator(news_queryset, self.paginate_by)
        page = self.request.GET.get('page')
        context['news_queryset'] = news_queryset
        context['categories'] = Category.objects.all()
        context['page_counter'] = range(paginator.num_pages)
        return context