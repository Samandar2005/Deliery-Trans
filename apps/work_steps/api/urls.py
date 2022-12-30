from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.work_steps.api.v1.urls'))
]
