from django.contrib import admin
from college.models import Notice,Student
# Register your models here.
from django.contrib.admin.options import  ModelAdmin




class NoticeAdmin(ModelAdmin):
    list_display=["subject","cr_date"]
    list_filter=["cr_date"]
    search_fields=["subject","msg"]


class StudentAdmin(ModelAdmin):
    list_display=["name","address"]
    list_filter=["name"]
    search_fields=["address"]
# REGISTERING THE MODEL Notice 
admin.site.register(Notice)
admin.site.register(Student,StudentAdmin)

# to create teh superuser we are running the command
# python manage.py createsuperuser