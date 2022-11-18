from django.db import models


class CustomUser(models.Model):
    """
    A normal class that represents a User object, the attributes are those bellow:
    """
    f_name = models.CharField(
        verbose_name="First Name", max_length=30, default="Test")
    l_name = models.CharField(
        verbose_name="Last Name", max_length=30, default='Test')
    cpf = models.CharField(verbose_name="CPF", max_length=15)
    age = models.IntegerField(verbose_name="Age")
    email = models.EmailField(verbose_name="email", max_length=30)

    def __str__(self):
        return f"{self.f_name}"
