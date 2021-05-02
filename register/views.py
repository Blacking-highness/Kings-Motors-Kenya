from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(responce):
    if responce.method == "POST":
        form = RegisterForm(responce.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(responce, "register/register.html", context)

def bye_page(responce):
    context = {}
    return render(responce, "bye/bye.html", context)