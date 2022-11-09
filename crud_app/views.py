from django.shortcuts import render


def menu(request):
    return render(request, "menu.html")


def check_data(request):
    return render(check_data, "check_data.html")


def delete_data(request):
    return render(delete_data, "delete_data.html")


def register_user(request):
    return render(register_user, "register_user")


def update_data(request):
    return render(update_data, "update_data.html")
