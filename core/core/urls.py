"""
URL configuration for core project.

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
from django.urls import path, include
from rest_framework import routers
from main.views import CarView, CategoryView, UserView , CarListAPIView , CarDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'car', CarView)
router.register(r'category', CategoryView)
router.register(r'user', UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('car_list/', include(router.urls)),
    path('cars/' , CarListAPIView.as_view()),
    path('cars/delete/<int:pk>' , CarDestroyAPIView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
