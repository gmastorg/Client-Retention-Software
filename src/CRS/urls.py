"""CRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from pages.views import home_view, contact_view, about_view
from django.conf import settings
from django.conf.urls.static import static



#This is where you resolve a url to a view
urlpatterns = [
    path('', home_view, name="home"), 
    path('admin/', admin.site.urls),
    path('contact/', contact_view),
    path('about/', about_view),

    #must import include see above
    #allows you to put all products urls in their own urls.py file in products folder
    path("products/", include ("products.urls")),
    path("shows/", include ("shows.urls")),
    path("clients/", include ("clients.urls")),
    path("sectors/", include ("sectors.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
