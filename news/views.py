from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from news.models import News, Category
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from .forms import CommentForm
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy

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

class NewsDetailView(ModelFormMixin, DetailView):
    model = News
    template_name = 'news/news.html'
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        news = get_object_or_404(News, slug_news=kwargs['slug_news'])
        comments = news.comments.all()
        slug_news=kwargs['slug_news']
        return render(request, 'news/news.html', context={
            'news': news,
            'categories': Category.objects.all(),
            'comments': comments,
            'form': self.get_form(),
            })

    def get_success_url(self):
        return reverse_lazy('news', self.kwargs['slug_news'])

    def post(self, request, *args, **kwargs):
        news = get_object_or_404(News, slug_news=kwargs['slug_news'])
        form = self.get_form()
        comments = news.comments.all()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.news_name = news
            if request.user.is_authenticated:
                new_comment.username = request.user
                new_comment.save()
                message = 'Ваш комментарий успешно добавлен'
            else:
                message = 'Чтобы добавить комментарий пожалуйста войдите в систему'
            return render(request, 'news/news.html', context={
                'news': news,
                'categories': Category.objects.all(),
                'comments': comments,
                'form' : self.get_form(),
                'message': message,
                })
        else:
            return self.form_invalid(form)

