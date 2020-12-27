from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    content = models.TextField()

#class Register(User):
#    pass
#   # username = models.TextField()
# #   email = models.URLField(unique = True)  #key for making it mandatory
#    #password = models.CharField(max_length=12,validators=[MinLengthValidator(4)])
