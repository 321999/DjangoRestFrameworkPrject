from django.shortcuts import render
from  django.http import HttpResponse
# 
from rest_framework import viewsets


# The serialiser will basically serialise the thing by adding the hyperlinks 
from college.serialiser import NoticeSerialiser,StudentSerialiser
from college.models import Notice,Student
# from models import Notice
# Create your views here.
def home(self):
    return HttpResponse("hello")

def create(self):
    data=Notice.objects.get(id=2)
    print(data.msg)
    # for i in data:
    #     print(i.msg)
    return HttpResponse("within")


# creating  the modular  programing
'''
 A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions is ModelViewSet
'''
class NoticeViewSet(viewsets.ModelViewSet):
    # queryset has to  be there 
    queryset=Notice.objects.all()
    serializer_class=NoticeSerialiser


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerialiser
# this is homepage
def homepage(self):
    return HttpResponse("<h1>deskpage will </h1>")