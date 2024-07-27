from django.db import models

# Create your models here.
class myregister(models.Model):
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=80)
    course=models.CharField(max_length=50,default="bca")
    file=models.FileField(default="not available")

