"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from shamseya_task.core.views import home

api_urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("core/", include("shamseya_task.core.api.urls", namespace="core_api")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("", home, name="home"),
]

if getattr(settings, "DEBUG"):
    import debug_toolbar  # noqa

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
