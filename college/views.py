from django.shortcuts import render
from  django.http import HttpResponse
from rest_framework import viewsets


# The serialiser will basically serialise the thing by adding the hyperlinks 
from college.serialiser import NoticeSerialiser
from college.models import Notice
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
class NoticeViewSet(viewsets.ModelViewSet):
    queryset=Notice.objects.all()
    serializer_class=NoticeSerialiser



# this is homepage
def homepage(self):
    return HttpResponse("<h1>deskpage will </h1>")