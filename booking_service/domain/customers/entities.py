from datetime import datetime
from .exceptions import InvalidCustomerDocumentException, CustomerShouldBeOlderThan18


class Customer:
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

    def is_valid(self):
        if len(self.document) < 5:
            raise InvalidCustomerDocumentException("Invalid document number")
        elif (
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
