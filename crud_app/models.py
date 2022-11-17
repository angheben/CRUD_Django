from django.db import models


class User(models.Model):
    """
    A normal class that represents a User object, the attributes are those bellow:
    """
    first_name = models.CharField(verbose_name="First Name", name="First Name", max_length=30, default="Test")
    last_name = models.CharField(verbose_name="Last Name", name="Last Name", max_length=30, default='Test')
    cpf = models.CharField(verbose_name="CPF", name="CPF", max_length=15)
    age = models.IntegerField(verbose_name="Age", name="Age")
    email = models.EmailField(verbose_name="email", name="email", max_length=30)

    def __str__(self):
        return f"{self.first_name}"
