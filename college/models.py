from django.db import models

# Create your models here.
# Creatng   the notice class
class Notice(models.Model):
    subject=models.CharField(max_length=20)
    msg=models.TextField()
    date=models.DateField(auto_now_add=True)

# create a student model so that everyone will get the notice 
class Student(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    

    # msg=models.TextField()
    # date=models.DateField(auto_now_add=True)