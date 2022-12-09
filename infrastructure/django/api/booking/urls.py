from django.urls import path

from .views import BookingViewSet

urlpatterns = [
    path(
        "booking",
        BookingViewSet.as_view(
            {
                "post": "create",
            }
        ),
    ),
]
