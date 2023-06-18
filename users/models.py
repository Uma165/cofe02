from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    imag = models.ImageField(upload_to='users_images', null=True, blank=True)
