from datetime import datetime
from .exceptions import (
    InvalidCustomerDocumentException,
    CustomerShouldBeOlderThan18,
    MissingParamError,
)


class Customer:
    name: str
    birth_date: datetime
    document: str
    email: str
    id: str | None

    def __init__(
        self,
        name: str,
        birth_date: datetime,
        document: str,
        email: str,
        id: str | None = None,
    ) -> None:
        self.name = name
        self.birth_date = birth_date
        self.document = document
        self.email = email
        self.id = id

    def create_customer(self):
        self.is_valid()

    def is_valid(self):
        required_fields = ["name", "birth_date", "document", "email"]
        for field in required_fields:
            if getattr(self, field) is None:
                raise MissingParamError(field)
        if len(self.document) < 5:
            raise InvalidCustomerDocumentException("Invalid document number")
        if (
            datetime.today().year
            - self.birth_date.year
            - (
                (self.birth_date.month, self.birth_date.day)
                < (self.birth_date.month, self.birth_date.day)
            )
            < 18
        ):
            raise CustomerShouldBeOlderThan18("Customer should be older than 18")
        return True
