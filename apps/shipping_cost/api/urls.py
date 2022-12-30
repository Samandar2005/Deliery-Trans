from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.shipping_cost.api.v1.urls'))
]
