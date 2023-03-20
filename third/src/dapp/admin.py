from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titles', 'Category', 'pub_date', 'modified_date', 'slug', 'post_status')
    list_display_links = ('titles',)
    list_filter = ('pub_date', 'Category', 'Tag')
    search_fields = ('titles', 'content')

    def get_ordering(self, request):
        return ['-pub_date']

    def titles(self, obj):
        return obj.titles

    def content(self, obj):
        return obj.content
    
    def Category(self, obj):
        return obj.Category

    def pub_date(self, obj):
        return obj.pub_date

    def modified_date(self, obj):
        return obj.modified_date

    def slug(self, obj):
        return obj.slug
    
    def post_status(self, obj):
        return obj.post_status

    titles.short_description = 'Title'
    content.short_description = 'Content'
    Category.short_description = 'Category'
    pub_date.short_description = 'Published date'
    modified_date.short_description = 'Last modified'
    slug.short_description = 'Slug'
    post_status.short_description = 'post_status'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('titles', 'slug')
    list_display_links = ('titles',)
    search_fields = ('titles',)

    def titles(self, obj):
        return obj.titles

    def slug(self, obj):
        return obj.slug

    titles.short_description = 'Title'
    slug.short_description = 'Slug'

class TagAdmin(admin.ModelAdmin):
    list_display = ('titles', 'slug')
    list_display_links = ('titles',)
    search_fields = ('titles',)

    def titles(self, obj):
        return obj.titles

    def slug(self, obj):
        return obj.slug

    titles.short_description = 'Title'
    slug.short_description = 'Slug'

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Blog_details)
