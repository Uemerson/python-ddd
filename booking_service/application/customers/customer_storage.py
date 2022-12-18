from abc import ABC, abstractmethod

from .customer_dto import CustomerDto


class CustomerStorage(ABC):
    @abstractmethod
    def save_customer(self, customer_dto: CustomerDto):
        raise NotImplementedError

    @abstractmethod
    def get_customer_by_id(self, id: str) -> CustomerDto:
        raise NotImplementedError

    @abstractmethod
    def get_all_customers(self) -> list[CustomerDto]:
        raise NotImplementedError
