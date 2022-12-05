import unittest
from datetime import datetime, timedelta
from booking_service.domain.booking.exceptions import (
    CheckinDateCannotBeAfterCheckoutDate,
)
from booking_service.domain.booking.entities import Booking
from booking_service.domain.customers.entities import Customer


class BookingAggregateTests(unittest.TestCase):
    def test_exception_message_checkin_cannot_be_after_checkout(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
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
        customer = Customer("valid_name", birth_date, "valid_document", "valid_email")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)
        with self.assertRaises(CheckinDateCannotBeAfterCheckoutDate) as ex:
            booking.is_valid()
        exception = ex.exception
        self.assertEqual(exception.message, "Checkin cannot be after Checkout")

    def test_checkin_date_cannot_be_after_checkout_date(self):
        checkin = datetime.utcnow()
        checkout = datetime.today() - timedelta(days=1)
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
        customer = Customer("valid_name", birth_date, "valid_document", "valid_email")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)
        self.assertRaises(CheckinDateCannotBeAfterCheckoutDate, booking.is_valid)
