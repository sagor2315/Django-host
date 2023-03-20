# from django.contrib import admin
# from .models import blog

# # Register your models here.
# admin.site.register(blog)

from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('titles', 'category', 'pubdate', 'modified', 'slug', 'post_status')
    list_display_links = ('titles',)
    list_filter = ('category',)
    search_fields = ('titles', 'content')

    def get_ordering(self, request):
        return ['-pubdate']

    def titles(self, obj):
        return obj.titles

    def content(self, obj):
        return obj.content

    def category(self, obj):
        return obj.category

    def pubdate(self, obj):
        return obj.pubdate

    def modified(self, obj):
        return obj.modified

    def slug(self, obj):
        return obj.slug
    
    def post_status(self, obj):
        return obj.post_status 

    titles.short_description = 'Title'
    content.short_description = 'Content'
    category.short_description = 'Category'
    pubdate.short_description = 'Published date'
    modified.short_description = 'Last modified'
    slug.short_description = 'Slug'
    slug.short_description = 'post_status'

admin.site.register(blog, BlogAdmin)
