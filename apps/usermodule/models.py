from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True    )

    user_permissions = models.ManyToManyField(
         'auth.Permission',
         related_name='customuser_set',
          blank=True    )
    def __str__(self):        return self.username


class Address(models.Model):
        city = models.CharField(max_length=100)

        def __str__(self):
            return self.city

class Student(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        address = models.ForeignKey(Address, on_delete=models.CASCADE)

        def __str__(self):
            return self.name
