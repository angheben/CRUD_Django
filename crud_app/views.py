from django.shortcuts import render


def menu(request):
    return render(request, "menu.html")


def check_data(request):
    return render(request, "check_data.html")


def delete_data(request):
    return render(request, "delete_data.html")


def register_user(request):
    return render(request, "register_user")


def update_data(request):
    return render(request, "update_data.html")
