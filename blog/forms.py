from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class SignInForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]
