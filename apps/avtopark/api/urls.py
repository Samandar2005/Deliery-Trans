from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.avtopark.api.v1.urls'))
]
