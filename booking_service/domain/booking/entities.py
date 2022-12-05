from datetime import datetime
from booking_service.domain.customers.entities import Customer
from .exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank


class Booking:
    checkin: datetime
    checkout: datetime
    customer: Customer

    def __init__(self, checkin: datetime, checkout: datetime, customer: Customer):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def create_booking(self):
        self.is_valid()

    def is_valid(self):
        if self.checkin > self.checkout:
            raise CheckinDateCannotBeAfterCheckoutDate(
                "Checkin cannot be after Checkout"
            )
        elif not self.customer:
            raise CustomerCannotBeBlank("Customer is a required information")

        self.customer.is_valid()

        return True
