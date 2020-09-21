from django.urls import path
from django.contrib.auth import views

from .views import *

urlpatterns = [
    path("", ArticleListView.as_view(), name="index"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("authentication/", AuthenticationView.as_view(), name="authentication"),
    path("logout/", LogoutView.as_view(), name="log_out"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("comment/<int:pk>/", CommentArticleView.as_view(), name="add_comment"),
    path("activate/<uidb64>/<token>/<timestamp>/", ActivateAccount.as_view(), name="activate")
]