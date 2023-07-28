"""
URL configuration for vishalaksha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path



from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from django.views.defaults import server_error
# from .views import custom_error_view

#google authentication


from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from django.contrib import admin

admin.site.site_header = 'Admin'
#Add the below line
admin.site.index_title = 'Autobot robotics'
# from django.urls import handler500

# ...
# handler500 = custom_error_view
from realstate import realviews



urlpatterns = [
    path('realstate/',realviews.index, name='realstate'),
    path('about', realviews.about, name='about'),
    path('contact', realviews.contact, name='contact'),
    path('services', realviews.services, name='services'),
    path('properties', realviews.properties, name='properties'),
    path('property', realviews.property, name='property'),
    path('property_details/<slug:slug>/', realviews.property, name='property_details'),
    path('blog', realviews.blog, name='blog'),
    path('blog_details/<slug:slug>/', realviews.blogdetails, name='blog_details'),
    path('search', realviews.search, name='search'),
   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# img src = {%%}