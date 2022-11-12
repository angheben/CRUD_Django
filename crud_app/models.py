from django.db import models


class User(models.Model):
    """
    A normal class that represents a User object, the attributes are those bellow:
    """
    first_name = models.CharField(name="First_Name", max_length=30)
    last_name = models.CharField(name="Last Name", max_length=30, default='Test')
    cpf = models.CharField(name="CPF", max_length=15)
    age = models.IntegerField(name="Age")
    email = models.EmailField(name="email", max_length=30)
