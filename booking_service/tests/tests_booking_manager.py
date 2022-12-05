import unittest
from datetime import datetime
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto
from booking_service.application.booking.booking_manager import BookingManager


class BookingAggregateManagerTests(unittest.TestCase):
    def test_create_booking(self):
        checkin = datetime.today()
        checkout = datetime.today()
        birth_date = datetime(
            datetime.today().year - 18,
            datetime.today().month,
            datetime.today().day,
            datetime.today().hour,
            datetime.today().minute,
            datetime.today().second,
            datetime.today().microsecond,
            datetime.today().tzinfo,
        )
        customer = CustomerDto(
            "valid_name", birth_date, "valid_document", "valid_email"
        )
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager()
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res["code"], "SUCCESS")
