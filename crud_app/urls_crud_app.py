from django.urls import path
from crud_app.views import update_data, check_data, delete_data, register_user, menu

urlpatterns = [
    path('', menu),
    path("check_data.html", check_data, name="change_data"),
    path("delete_data.html", delete_data, name="delete_data"),
    path("register_user", register_user, name="register_user"),
    path("update_data", update_data, name="update_data"),
]
