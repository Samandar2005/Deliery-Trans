from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.about.api.v1.urls'))
]
