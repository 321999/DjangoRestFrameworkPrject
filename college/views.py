from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def home(self):
    return HttpResponse("hello")

def create(self):
    return HttpResponse("within")

# this is homepage
def homepage(self):
    return HttpResponse("<h1>deskpage will </h1>")