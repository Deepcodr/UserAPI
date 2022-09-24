from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    UserID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    EmailID=models.EmailField(unique=True)
    Age=models.IntegerField()
    Address=models.TextField()