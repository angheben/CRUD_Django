from django.db import models


class User(models.Model):
    """
    A normal class that represents a User object, the attributes are those bellow:
    """
    first_name = models.CharField(name="First Name", max_length=30)
    last_name = models.CharField(name="Last Name", max_length=30)
    cpf = models.CharField(name="CPF", max_length=30)
    age = models.IntegerField(name="Age")
    email = models.EmailField(name="email", max_length=30)

    def __str__(self):
        return f"{self.first_name}"
