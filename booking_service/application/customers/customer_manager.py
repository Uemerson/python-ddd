from booking_service.domain.customers.exceptions import (
    CustomerShouldBeOlderThan18,
    InvalidCustomerDocumentException,
    MissingParamError,
)
from booking_service.helpers.http_helper import bad_request, created, ok, server_error

from .customer_dto import CustomerDto
from .customer_storage import CustomerStorage


class CustomerManager:
    storage: CustomerStorage

    def __init__(self, storage: CustomerStorage) -> None:
        self.storage = storage

    def create_new_customer(self, customer_dto: CustomerDto):
        try:
            customer_aggregate = customer_dto.to_domain()
            customer_aggregate.create_customer()
            self.storage.save_customer(customer_dto.to_dto(customer_aggregate))
            return created()
        except (
            CustomerShouldBeOlderThan18,
            InvalidCustomerDocumentException,
            MissingParamError,
        ) as ex:
            return bad_request(ex)
        except Exception:
            return server_error()

    def get_customer_by_id(self, customer_id: str):
        customer = self.storage.get_customer_by_id(customer_id)
        return ok(data=customer)

    def get_all_customers(self):
        customers = self.storage.get_all_customers()
        return ok(data=customers)
