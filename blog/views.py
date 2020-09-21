from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import logout, login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from datetime import datetime

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from .models import Article, ControlModel
from .forms import RegistrationForm, SignInForm, CommentForm
from .tokens import account_activation_token


class ArticleListView(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    queryset = model.objects.order_by("-datetime")


class ArticleDetailView(DetailView):
    model = Article
    slug_field = "url"


class RegistrationView(View):
    form_class = RegistrationForm
    template_name = "registration/registration.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = "Activate your account"
            message = render_to_string("registration/activation_email.html", {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
                "timestamp": datetime.now(),
            })
            user.email_user(subject, message)

        return render(request, self.template_name, {"form": form})


class ActivateAccount(View):

    link_duration = ControlModel.objects.get(name="duration").link_duration

    def get(self, request, uidb64, token, timestamp, *args, **kwargs):

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        timedelta = datetime.now() - datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        if timedelta > self.link_duration:
            user.delete()
            return HttpResponse("Sorry, the link is expired")

        if not user.is_active:
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                login(request, user)
                return redirect("index")
            else:
                return redirect("index")
        else:
            return HttpResponse("User is already created, use login")


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
