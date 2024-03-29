"""
URL configuration for MLOOPS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path, include

# redirectview is used to redirecting  the folder 
from django.views.generic.base import RedirectView

# from django.conf.urls import url
# from college import urls

urlpatterns = [
    path('admin/', admin.site.urls),

# when we dont have any other route that time we use redirectview 
# so this will lend to us college url and that college url when there is no route is there that time blank route in college url 
    path('',RedirectView.as_view(url='college/')),
    #  path("college/",RedirectView.as_view(url="/home/")),

    path("college/",include("college.urls")),
    # path("college/",include("college.urls")),

]

'''

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
'''