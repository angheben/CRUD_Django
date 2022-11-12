from django.urls import path
from crud_app.views import update_user, check_user, delete_user, register_user, menu

urlpatterns = [
    path('', menu),
    path("check_user.html", check_user, name="change_data"),
    path("delete_user.html", delete_user, name="delete_data"),
    path("register_user", register_user, name="register_user"),
    path("update_user", update_user, name="update_data"),
]
