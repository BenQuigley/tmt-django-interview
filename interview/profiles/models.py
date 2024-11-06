from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)  # hashed and salted
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
