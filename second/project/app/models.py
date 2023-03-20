from django.db import models
from django.utils.text import slugify

# Create your models here.

class blog(models.Model):
    category_drop_down = [('G', 'General'), ('S', 'Scrubber'), ('B', 'Brush'), ('BM', 'Bath Bomb'), ('BP', 'Bath Pillow')]
    status = [(0, 'Draft'),(1, 'Publish')]

    titles = models.CharField(max_length=200, null=True, blank=False, help_text = "Enter your title here", verbose_name='Title')
    content = models.TextField(help_text = "Enter your title here", verbose_name='Content')
    post_status = models.IntegerField(choices=status, default=0)
    category = models.CharField(max_length=3, choices=category_drop_down, verbose_name='Category')
    pubdate = models.DateTimeField(auto_now_add=True, verbose_name='Published date')
    modified = models.DateTimeField(auto_now=True, verbose_name='Last modified')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='Slug')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image')


    def __str__(self):
        return self.titles

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titles)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Blog entries'