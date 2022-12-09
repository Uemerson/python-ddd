from booking_service.application.booking.booking_storage import BookingStorage
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto
from .models import Customer, Booking
from django.db import transaction


class BookingRepository(BookingStorage):
    def _customer_dto_to_model(self, customer_dto: CustomerDto) -> Customer:
        customer = Customer()
        customer.name = customer_dto.name
        customer.birth_date = customer_dto.birth_date
        customer.document = customer_dto.document
        customer.email = customer_dto.email
        customer.id = customer_dto.id
        return customer

    def _booking_dto_to_model(self, booking_dto: BookingDto) -> Booking:
        booking = Booking()
        booking.checkin = booking_dto.checkin
        booking.checkout = booking_dto.checkout
        return booking

    @transaction.atomic
    def save_booking(self, booking_dto: BookingDto) -> None:
        customer = self._customer_dto_to_model(booking_dto.customer)
        customer.save()
        booking = self._booking_dto_to_model(booking_dto)
        booking.customer = customer
        booking.save()
