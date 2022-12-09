class CustomerShouldBeOlderThan18(Exception):
    def __init__(self, message):
        self.message = message


class InvalidCustomerDocumentException(Exception):
    def __init__(self, message):
        self.message = message


class MissingParamError(Exception):
    def __init__(self, param_name):
        super().__init__(f"Missing param: {param_name}")
