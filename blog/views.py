from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, FormView, View
from .models import Article, Comment, User
from .forms import RegistrationForm, SignInForm, CommentForm


class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    queryset = model.objects.order_by("-datetime")


class ArticleDetailView(DetailView):
    model = Article
    slug_field = "url"


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("authentication")


class AuthenticationView(LoginView):
    form_class = SignInForm
    template_name = "registration/login.html"


class LogoutView(View):

    def get(self, request):
        logout(request)

        return redirect("index")


class CommentArticleView(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        article = Article.objects.get(id=pk)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.author = user
            form.article = article
            form.save()
        return redirect(article.get_absolute_url())


