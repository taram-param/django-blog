from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=250, help_text="Enter valid email address")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control mb-3"})

    def as_p(self):
        return self._html_output(
            normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s %(errors)s</div>',
            error_row=u'<div class="error">%s</div>',
            row_ender='</div>',
            help_text_html=u'<div class="help-text">%s</div>',
            errors_on_separate_row=False)


class SignInForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]
