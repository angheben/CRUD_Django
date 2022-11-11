from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User


def menu(request):
    return render(request, "menu.html")


def check_data(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "check_data.html", context)


def delete_data(request):
    return render(request, "delete_data.html")


def register_user(request):
    return render(request, "register_user.html")


def update_data(request):
    return render(request, "update_data.html")
