from django.shortcuts import render
from django.views.generic import ListView
from news.models import News, Category


# Create your views here.


class NewsListView(ListView):
    model = News
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['last_news'] = News.objects.all()[:4]
        context['other_news'] = News.objects.all()[4:]
        context['categories'] = Category.objects.all()
        return context

