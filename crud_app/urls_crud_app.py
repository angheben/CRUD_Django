from django.urls import path
from crud_app.views import update_user, check_user, delete_user, register_user, menu

urlpatterns = [
    path('', menu),
    path("check_user.html", check_user, name="check_user.html"),
    path("register_user.html", register_user, name="register_user.html"),
    path("update_user.html", update_user, name="update_user.html"),
    path("delete_user.html", delete_user, name="delete_user.html")
]
