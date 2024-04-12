from django.shortcuts import render
from .forms import RegisterForm, EditForm
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
    message = ""
    if request.method == "POST":
        form = EditForm(request.POST, user=request.user)
        if form.is_valid():
            form.save(request.user)
            message = "Your changes have been saved!"
    else:
        form = EditForm(user=request.user)

    return render(request, "accounts/profile.html", {
        "message": message,
        "form": form
    })
