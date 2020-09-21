from django.contrib import admin
from .models import Article, Comment, ControlModel


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article")


@admin.register(ControlModel)
class ControlAdmin(admin.ModelAdmin):
    list_display = ("name", "link_duration")
