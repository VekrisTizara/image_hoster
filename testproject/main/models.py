from django.db import models
from userauth.models import User


class Image(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



