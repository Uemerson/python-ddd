import unittest
from datetime import datetime

from booking_service.application.customers.customer_dto import CustomerDto
from booking_service.application.customers.customer_manager import CustomerManager
from booking_service.application.customers.customer_storage import CustomerStorage
from booking_service.helpers.http_helper import bad_request, created, ok, server_error


class DummyStorage(CustomerStorage):
    def save_customer(self, customer_dto: CustomerDto):
        return True

    def get_customer_by_id(self, id: str) -> CustomerDto:
        return CustomerDto(
            id=id,
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

    def get_all_customers(self) -> list[CustomerDto]:
        return [
            CustomerDto(
                id="valid_id",
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
        ]


class CustomersManagerTests(unittest.TestCase):
    def setUp(self):
        self.dummy_storage = DummyStorage()

    def test_should_bad_request_if_an_invalid_customer_is_provider(self):
        customer_dto = CustomerDto(
            name=None,
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
        manager = CustomerManager(self.dummy_storage)
        response = manager.create_new_customer(customer_dto)
        self.assertEqual(response, bad_request(response["body"]))

    def test_should_created_if_a_valid_customer_is_provider(self):
        customer_dto = CustomerDto(
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
        manager = CustomerManager(self.dummy_storage)
        response = manager.create_new_customer(customer_dto)
        self.assertEqual(response, created())

    def test_should_server_error_if_create_new_customer_throws(self):
        customer_dto = CustomerDto(
            name="valid_name",
            birth_date="invalid",
            document="valid_document",
            email="valid_email",
        )
        manager = CustomerManager(self.dummy_storage)
        http_response = manager.create_new_customer(customer_dto)
        self.assertEqual(http_response["statusCode"], 500)
        self.assertEqual(str(http_response["body"]), str(server_error()["body"]))

    def test_should_return_ok_if_get_all_customers(self):
        manager = CustomerManager(self.dummy_storage)
        http_response = manager.get_all_customers()
        self.assertEqual(
            http_response,
            ok(http_response["body"]),
        )


if __name__ == "__main__":
    unittest.main()
