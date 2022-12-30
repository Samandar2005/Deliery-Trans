from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.client.api.v1.urls'))
]
