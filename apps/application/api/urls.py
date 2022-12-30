from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.application.api.v1.urls'))
]
