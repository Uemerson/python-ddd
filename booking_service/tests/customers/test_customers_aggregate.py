import unittest
from datetime import datetime
from booking_service.domain.customers.exceptions import (
    MissingParamError,
    InvalidCustomerDocumentException,
    CustomerShouldBeOlderThan18,
)
from booking_service.domain.customers.entities import Customer


class CustomersAggregateTests(unittest.TestCase):
    def test_should_raise_missing_param_error_if_no_name_is_provided(self):
        customer = Customer(
            name=None,
            birth_date=datetime.utcnow(),
            document="any_document",
            email="any_email",
        )
        self.assertRaises(MissingParamError, customer.is_valid)

    def test_should_raise_missing_param_error_if_no_birth_date_is_provided(self):
        customer = Customer(
            name="valid_name",
            birth_date=None,
            document="valid_document",
            email="valid_email",
        )
        self.assertRaises(MissingParamError, customer.is_valid)

    def test_should_raise_missing_param_error_if_no_document_is_provided(self):
        customer = Customer(
            name="valid_name",
            birth_date=datetime.utcnow(),
            document=None,
            email="valid_email",
        )
        self.assertRaises(MissingParamError, customer.is_valid)

    def test_should_raise_missing_param_error_if_no_email_is_provided(self):
        customer = Customer(
            name="valid_name",
            birth_date=datetime.utcnow(),
            document="valid_document",
            email=None,
        )
        self.assertRaises(MissingParamError, customer.is_valid)

    def test_should_raise_invalid_customer_document_exception_if_an_invalid_document_is_provided(
        self,
    ):
        customer = Customer(
            name="valid_name",
            birth_date=datetime.utcnow(),
            document="",
            email="valid_email",
        )
        self.assertRaises(InvalidCustomerDocumentException, customer.is_valid)

    def test_should_raise_customer_should_be_older_than_18_if_an_invalid_birth_date_is_provided(
        self,
    ):
        customer = Customer(
            name="valid_name",
            birth_date=datetime.utcnow(),
            document="valid_document",
            email="valid_email",
        )
        self.assertRaises(CustomerShouldBeOlderThan18, customer.is_valid)

    def test_should_return_true_if_valid_customer_is_provided(
        self,
    ):
        customer = Customer(
            name="valid_name",
            birth_date=datetime(
                datetime.utcnow().year - 20,
                datetime.utcnow().month,
                datetime.utcnow().day,
                datetime.utcnow().hour,
                datetime.utcnow().minute,
                datetime.utcnow().second,
                datetime.utcnow().microsecond,
                datetime.utcnow().tzinfo,
            ),
            document="valid_document",
            email="valid_email",
        )
        self.assertTrue(customer.is_valid())


if __name__ == "__main__":
    unittest.main()
