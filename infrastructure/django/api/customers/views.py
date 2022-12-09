from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import dateparse

from booking_service.application.customers.customer_dto import CustomerDto
from booking_service.application.customers.customer_manager import CustomerManager
from .repositories import CustomerRepository


class CustomerViewSet(viewsets.ViewSet):
    def create(self, request):
        name, birth_date, document, email = [
            request.data.get(k, None)
            for k in ("name", "birth_date", "document", "email")
        ]
        dto = CustomerDto(
            name=name,
            birth_date=dateparse.parse_datetime(birth_date),
            document=document,
            email=email,
        )
        customer_repository = CustomerRepository()
        customer_manager = CustomerManager(customer_repository)
        http_response = customer_manager.create_new_customer(dto)
        return Response(
            http_response["body"]
            if http_response["statusCode"] >= 200 and http_response["statusCode"] <= 299
            else {"error": str(http_response["body"])},
            status=http_response["statusCode"],
        )
