from django.db import models

#GOTO video 11:13 for more
class User(models.Model):
    name: models.CharField(max_length=50)
    email: models.CharField(max_length=50)
