from django.db import transaction

from booking_service.application.customers.customer_dto import CustomerDto
from booking_service.application.customers.customer_storage import CustomerStorage

from .models import Customer


class CustomerRepository(CustomerStorage):
    def _customer_dto_to_model(self, customer_dto: CustomerDto) -> Customer:
        customer = Customer()
        customer.name = customer_dto.name
        customer.birth_date = customer_dto.birth_date
        customer.document = customer_dto.document
        customer.email = customer_dto.email
        customer.id = customer_dto.id
        return customer

    def _model_to_dto(self, customer: Customer):
        return CustomerDto(
            name=customer.name,
            birth_date=customer.birth_date,
            document=customer.document,
            email=customer.email,
            id=customer.id,
        )

    @transaction.atomic
    def save_customer(self, customer_dto: CustomerDto) -> None:
        customer = self._customer_dto_to_model(customer_dto)
        customer.save()

    def get_customer_by_id(self, id: str) -> CustomerDto:
        customer = Customer.objects.get(id=id)
        return self._model_to_dto(customer)

    def get_all_customers(self) -> list[CustomerDto]:
        customers = Customer.objects.all()
        customers_dto: list[CustomerDto] = []
        for customer in customers:
            customers_dto.append(self._model_to_dto(customer))
        return customers_dto
