from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User


def menu(request):
    return render(request, "menu.html")


def check_user(request):
    users = User.objects.all()
    return render(request, "check_user.html", {"users": users})


def register_user(request):
    return render(request, "register_user.html")


def update_user(request):
    return render(request, "update_user.html")


def delete_user(request):
    return render(request, "delete_user.html")
