from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime

from booking_service.application.booking.booking_dto import BookingDto
from .repositories import BookingRepository

# from .models import Booking


class BookingViewSet(viewsets.ViewSet):
    def create(self, request):
        checkin = datetime.strptime(request.POST.get("checkin"), "%Y-%m-%dT%H:%M")
        checkout = datetime.strptime(request.POST.get("checkout"), "%Y-%m-%dT%H:%M")

        # serializer = ProductSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # publish("product_created", serializer.data)
        # return Response(serializer.data, status.HTTP_201_CREATED)

        return Response({"ok": "ok"})

        # customer_dto = get_customer_from_request(request)

        # dto = BookingDto(checkin, checkout, customer_dto)
        # repository = BookingRepository()
        # manager = BookingManager(repository)
        # res = manager.create_new_booking(dto)

        # if res["code"] != "SUCCESS":
        #     return render(request, "index.html", {"res": res})
        # else:
        #     return render(request, "confirmation.html")
