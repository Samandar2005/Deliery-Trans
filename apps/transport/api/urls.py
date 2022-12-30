from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.transport.api.v1.urls'))
]
