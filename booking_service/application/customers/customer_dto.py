from datetime import datetime
from booking_service.domain.customers.entities import Customer


class CustomerDto:
    name: str
    birth_date: datetime
    document: str
    email: str

    def __init__(
        self, name: str, birth_date: datetime, document: str, email: str
    ) -> None:
        self.name = name
        self.birth_date = birth_date
        self.document = document
        self.email = email

    def to_domain(self):
        return Customer(self.name, self.birth_date, self.document, self.email)

    def to_dto(self, customer: Customer):
        return CustomerDto(
            name=customer.name,
            birth_date=customer.birth_date,
            document=customer.document,
            email=customer.email,
        )
