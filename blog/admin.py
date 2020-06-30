from django.contrib import admin
from .models import Post,Comment,SubScribers
# Register your models here.


@admin.register(Post)
class Post_admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class Comment_admin(admin.ModelAdmin):
    list_display = ('name','body','post','active')
    list_filter = ('name','body','post','active')
    search_fields = ('post__title',)



@admin.register(SubScribers)
class subs_admin(admin.ModelAdmin):
    list_display = ('name','emails')
    list_filter = ('name','emails')
    search_fields = ('name','emails')