from django.db import models

# Create your models here.

class user_info(models.Model):

    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Email=models.EmailField(unique=True)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name
