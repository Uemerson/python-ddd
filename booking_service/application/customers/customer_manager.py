from .customer_storage import CustomerStorage
from booking_service.domain.customers.exceptions import (
    CustomerShouldBeOlderThan18,
    InvalidCustomerDocumentException,
    MissingParamError,
)
from .customer_dto import CustomerDto
from booking_service.helpers.http_helper import created, bad_request, server_error, ok


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
