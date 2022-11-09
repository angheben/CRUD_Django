from django.db import models


class User(models.Model):
    """
    A normal class that represents an User object, the atributes are those bellow:
    """
    first_name = models.CharField(name="First Name", max_length=30)
    last_name = models.CharField(name="Last Name", max_length=30)
    cpf = models.CharField(name="CPF", max_length=30)
    age = models.IntegerField(name="Age")
    email = models.EmailField(name="email", max_length=30)

    def __str__(self):
        """
        It's commun to use this method to show the atributes and information of your class in the admin.py file
        """
        return self.first_name, self.last_name, self.cpf, self.age, self.email


