from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article")
