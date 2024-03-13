from django.urls import  path,include
from django.views.generic.base import RedirectView
# from django.conf.urls import url
from college import views

urlpatterns=[
    path("home/",views.home,name="home.py"),
    # whenever the path is blank it will route  to someanother page 
path('',RedirectView.as_view(url='/home/')),
    # path("college/",RedirectView.as_view(url="college/ home/")),
]