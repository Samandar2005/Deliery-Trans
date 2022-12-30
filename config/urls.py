"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Deliery Trans",
        default_version='v1',
        description="Deliery Trans official site description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="samandarboriyev2005@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += [
    # admin
    path('admin/', admin.site.urls),

    # local urls
    # path('account/', include('apps.account.api.urls')),
    path('about/', include('apps.about.api.urls')),
    path('application/', include('apps.application.api.urls')),
    path('avtopark/', include('apps.avtopark.api.urls')),
    path('blog/', include('apps.blog.api.urls')),
    path('client/', include('apps.client.api.urls')),
    path('shipping_cost/', include('apps.shipping_cost.api.urls')),
    path('transport/', include('apps.transport.api.urls')),
    path('work_steps/', include('apps.work_steps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)