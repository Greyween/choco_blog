from django.contrib import admin

from .models import Category, Post, Comment
from account.models import Profile


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'created')
	list_filter = ('name', 'created')
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'created')
	list_filter = ('created', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'created', 'publish', 'status')
	list_filter = ('created', 'updated', 'publish')
	search_fields = ('author', 'body')

admin.site.register(Comment, CommentAdmin)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'karma')

admin.site.register(Profile, ProfileAdmin)	