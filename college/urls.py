from django.urls import  path,include
from django.views.generic.base import RedirectView
# from django.conf.urls import url
from college import views

urlpatterns=[
    path('',RedirectView.as_view(url='/kishre')),
    path("home/",views.home,name="home.py"),
    # whenever the path is blank it will route  to someanother page 

    path('kishre/',views.create,name="kishre"),
# in the college the path when  there is nothing it wil redirect to the kishore path
path("homepage/",views.homepage,name="homepage"),

# path('',RedirectView.as_view(url='/kishre/')),
# path("college/",RedirectView.as_view(url="college/ home/")),
]