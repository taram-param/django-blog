from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver


class Article(models.Model):

    title = models.CharField("title", max_length=150)
    content = models.TextField("content")
    datetime = models.DateTimeField("post date", auto_now_add=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.url})

    def get_comment(self):
        return self.comment_set.all()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.TextField("comment", max_length=500)
    datetime = models.DateTimeField("comment date", auto_now_add=True)
    article = models.ForeignKey(Article, verbose_name="article", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} - {self.article}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
