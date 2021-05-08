from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from store.models import Customer
from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your views here.
def register(responce):
    if responce.method == "POST":
        form = RegisterForm(responce.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )

            new_user_ = User.objects.filter()
            

            new_customer = Customer.objects.create(user=new_user_,
                           name = form.cleaned_data['username'],
                           email = form.cleaned_data['email'],)
            login(request, new_user)
        
        return redirect('/')
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(responce, "register/register.html", context)

def bye_page(responce):
    context = {}
    return render(responce, "bye/bye.html", context)

