from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Blog_details(models.Model):
    blog_name = models.CharField(max_length=100)
    details = models.CharField(max_length=50)

    def __str__(self):
        return self.blog_name

class Tag(models.Model):
    titles = models.CharField(max_length=200, blank=True, null=True, help_text='Ente your titles name', verbose_name='Titles')
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.titles
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titles)
        super().save(*args, **kwargs)


class Category(models.Model):
    titles = models.CharField(max_length=200, blank=True, null=True, help_text='Ente your titles name', verbose_name='Titles')
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.titles

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titles)
        super().save(*args, **kwargs)

class Post(models.Model):

    status = [(0, 'Draft'),(1, 'Publish')]

    titles = models.CharField(max_length=200, blank=True, null=True, help_text='Enter your title name', verbose_name='Titles')
    content = RichTextField(blank=True, null=True, verbose_name='Content')

    Category = models.ForeignKey(Category, on_delete= models.SET_NULL, blank=True, null=True, verbose_name='category')

    Tag = models.ManyToManyField(Tag, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='Modified Date')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name='Slug')
    post_status = models.IntegerField(choices=status, default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Image')
    featured = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titles
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titles)
        super().save(*args, **kwargs) 