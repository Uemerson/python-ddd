from abc import ABC, abstractmethod
from .customer_dto import CustomerDto


class CustomerStorage(ABC):
    @abstractmethod
    def save_customer(self, customer_dto: CustomerDto):
        pass

    @abstractmethod
    def get_customer_by_id(self, id: str) -> CustomerDto:
        pass
