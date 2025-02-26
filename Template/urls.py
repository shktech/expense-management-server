"""
URL configuration for expense_management_server project.

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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from Template.views import health_check

schema_view = get_schema_view(
    openapi.Info(
        title="Expense Management API",
        default_version='v1',
        description="API documentation for Expense Management",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', health_check, name='health-check'),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include('expenses.urls')),
        path('auth/', include('users.urls')),
        path('common/', include('common.urls')),
    ])),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]