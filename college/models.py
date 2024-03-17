from django.db import models

# Create your models here.
# Creatng   the notice class
class Notice(models.Model):
    subject=models.CharField(max_length=20)
    msg=models.TextField()
    date=models.DateField(auto_now_add=True)