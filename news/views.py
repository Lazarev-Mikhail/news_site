from django.shortcuts import render
from django.views.generic import ListView
from news.models import News, Category
from django.core.paginator import Paginator



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

