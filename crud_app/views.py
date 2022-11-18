from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import CustomUser


def menu(request):
    return render(request, "menu.html")


def register_user(request):
    return render(request, "register_user.html")


def check_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, "check_user.html", context)


def update_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, "update_user.html", context)


def delete_user(request):
    return render(request, template_name="delete_user.html")


def specific_user(request, pk):
    spec_user = CustomUser.objects.get(id=pk)
    context = {
        "spec_user": spec_user
    }
    return render(request, "specific_user.html", context=context)
