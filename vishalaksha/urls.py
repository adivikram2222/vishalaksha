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
from home import views



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







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('contact',views.contact, name = 'contact'),
    path('services',views.services, name = 'services'),
    path('about',views.about, name = 'about'),
    
    
    path('about',views.about, name = 'about'),
    path('about',views.about, name = 'about'),
    path('about',views.about, name = 'about'),
    
    
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# img src = {%%}