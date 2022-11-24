from django.urls import path
from crud_app.views import update_user, check_user, delete_user, register_user, menu, update_record, save

urlpatterns = [
    path('', menu),
    path("check_user.html", check_user, name="check_user.html"),
    path("register_user.html", register_user, name="register_user.html"),
    path("update_user.html", update_user, name="update_user.html"),
    path("delete_user.html", delete_user, name="delete_user.html"),
    path('update_record/<int:id>', update_record, name='update_record.html'),
    path('update_record/update_save/<int:id>', update_record, name='update_record.html'),
    path("save.html", save, name="save.html")
]
