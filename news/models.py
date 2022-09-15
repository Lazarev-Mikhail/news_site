from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

name_default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

content_default = '''

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vel dui enim. Duis molestie porta augue ac sodales. Fusce at nulla sit amet velit mattis porttitor. Aenean rhoncus nibh nulla, sed blandit ligula congue a. Vivamus id rhoncus sapien. Duis sit amet vulputate neque, accumsan tempus lacus. Vestibulum viverra sem condimentum accumsan maximus. Suspendisse venenatis sem nibh, non feugiat ex efficitur at. Ut ac elementum nisi. Nullam enim massa, porttitor ac elit id, convallis lobortis lectus. Nullam quis lobortis odio. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac odio libero.

Nullam arcu mauris, cursus sed sem at, lobortis condimentum odio. Quisque tincidunt est arcu. Curabitur porttitor blandit enim sed consectetur. Duis eu pretium ligula. Donec non leo est. Nullam malesuada urna sed odio rhoncus consectetur. Nunc lobortis quis nulla ac porta. Curabitur quis volutpat lacus.

Aliquam vehicula eleifend erat non sollicitudin. Nam eu risus dignissim, condimentum quam sed, lobortis sem. Curabitur tempor hendrerit interdum. Nunc in odio quis est accumsan condimentum. Morbi viverra pulvinar justo in dapibus. Nunc vel mauris et metus rhoncus dignissim. Integer ante metus, aliquet at pellentesque non, rutrum sodales augue. Vivamus ullamcorper vulputate eros, vitae hendrerit est. Pellentesque vehicula odio dolor, eu viverra dolor condimentum at. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec fermentum volutpat lorem eget ullamcorper. Morbi in sagittis tellus. Sed ut dolor et nulla malesuada molestie a et augue. Curabitur sit amet ipsum eget lorem hendrerit venenatis. Aenean sed eros purus. Sed dignissim odio eu mi porttitor, ac luctus lacus euismod.

Sed cursus orci quis felis volutpat, sit amet feugiat diam hendrerit. Suspendisse at nibh ac quam posuere sollicitudin. Ut eu porta enim, et consectetur augue. Praesent tempor venenatis eros sit amet mollis. Fusce sit amet porttitor dui. Maecenas in ex ut purus vulputate dictum sit amet a nulla. Pellentesque nec vestibulum nisi, eget ornare sem.

Curabitur nisl lorem, fermentum a tincidunt feugiat, pellentesque id tortor. In eget erat mi. Etiam ex risus, elementum ac nisl a, vestibulum interdum risus. Maecenas rhoncus faucibus purus, a suscipit orci. Duis tincidunt tempor nunc non feugiat. Curabitur porta, tortor eu pharetra pulvinar, risus est pulvinar dolor, nec porttitor metus elit in arcu. Aliquam erat volutpat. '''

class News(models.Model):

    name = models.CharField(max_length=150, default=name_default)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    null=True, related_name='news')
    image = models.FileField(upload_to='gallery')
    content = models.TextField(blank=False, default=content_default)
    time = models.DateTimeField(auto_now=True)
    slug_news = models.SlugField(default='', null=False, db_index=True)

    # def get_url(self):
    #     return reverse('one_news', args=[self.slug_news])

    def __str__(self):
        return f'{self.name}-{self.time}'
