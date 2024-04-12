from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditForm(forms.Form):
    username = forms.CharField(max_length=150) # Default max length for users is 150
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields["username"].initial = user.username
        self.fields["first_name"].initial = user.first_name
        self.fields["last_name"].initial = user.last_name
        self.fields["email"].initial = user.email

    def save(self, user):
        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
