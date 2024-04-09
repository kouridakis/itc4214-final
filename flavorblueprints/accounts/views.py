from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})
