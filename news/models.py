from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class News(models.Model):

    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    null=True, related_name='news')
    image = models.FileField(upload_to='gallery')
    content = models.TextField(blank=True)
    time = models.DateTimeField()
    slug_news = models.SlugField(default='', null=False, db_index=True)

    # def get_url(self):
    #     return reverse('one_news', args=[self.slug_news])

    def __str__(self):
        return f'{self.name}-{self.time}'
