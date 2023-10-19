from django.db import models
# from django.utils.dateformat import DateFormat

# Create your models here.
class Member(models.Model):
    name= models.CharField(max_length=20)
    parent=models.CharField(max_length=20)
    # dob=models.DateField(null=True)
    tel=models.IntegerField(null=True)
    course=models.CharField(max_length=20 ,null=True)
    adrs=models.CharField(max_length=100, null=True)
    district=models.CharField(max_length=20, null=True)
