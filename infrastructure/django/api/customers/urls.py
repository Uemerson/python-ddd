from django.urls import path

from .views import CustomerViewSet

urlpatterns = [
    path(
        "customer",
        CustomerViewSet.as_view(
            {
                "post": "create",
            }
        ),
    ),
]
