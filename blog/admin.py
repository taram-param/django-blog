from django.contrib import admin
from .models import Article, Comment, UserProfile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "article")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)

#admin.site.register(UserProfile)