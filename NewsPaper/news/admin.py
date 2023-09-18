from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, ScbscribersCategory

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(PostCategory)
# Register your models here.
