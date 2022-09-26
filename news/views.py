from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from news.models import News, Category, Comment
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django import forms


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
        context['category'] = category
        context['news_queryset'] = news_queryset
        context['categories'] = Category.objects.all()
        context['page_counter'] = range(paginator.num_pages)
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news.html'

    def get(self, request, *args, **kwargs):
        news = get_object_or_404(News, slug_news=kwargs['slug_news'])
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        comments = Comment.objects.all()
        return render(request, 'news/news.html', context={
            'num_visits': num_visits,
            'news': news,
            'categories': Category.objects.all(),
            'comments': comments,
        })
