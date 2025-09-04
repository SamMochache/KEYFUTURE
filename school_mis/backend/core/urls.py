"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from academics.views import ClassroomViewSet, SubjectViewSet

# Define the router and register your viewsets here
router = DefaultRouter()
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #Open API endpoints can be added here
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    #Authentication endpoints can be added here
    path('api/accounts/', include('accounts.urls')),
    #extend the router;
    path('api/', include(router.urls))
]
