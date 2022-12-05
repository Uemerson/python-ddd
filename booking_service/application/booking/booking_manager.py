from booking_service.domain.booking.exceptions import (
    CheckinDateCannotBeAfterCheckoutDate,
    CustomerCannotBeBlank,
)
from booking_service.domain.customers.exceptions import (
    CustomerShouldBeOlderThan18,
    InvalidCustomerDocumentException,
)
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import ErrorCodes, SuccessCodes


class BookingManager:
    def create_new_booking(self, booking_dto: BookingDto):
        booking_aggregate = booking_dto.to_domain()

        try:
            booking_aggregate.create_booking()
            return {
                "message": SuccessCodes.SUCCESS.value,
                "code": SuccessCodes.SUCCESS.name,
            }
        except CheckinDateCannotBeAfterCheckoutDate:
            return {
                "message": ErrorCodes.CHECKINAFTERCHECKOUT.value,
                "code": ErrorCodes.CHECKINAFTERCHECKOUT.name,
            }
        except CustomerCannotBeBlank:
            return {
                "message": ErrorCodes.CUSTOMERISREQUIRED.value,
                "code": ErrorCodes.CUSTOMERISREQUIRED.name,
            }
        except CustomerShouldBeOlderThan18:
            return {
                "message": ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.value,
                "code": ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.name,
            }
        except InvalidCustomerDocumentException:
            return {
                "message": ErrorCodes.INVALIDCUSTOMERDOCUMENT.value,
                "code": ErrorCodes.INVALIDCUSTOMERDOCUMENT.name,
            }

        except Exception:
            return {
                "message": ErrorCodes.UNDEFINED.value,
                "code": ErrorCodes.UNDEFINED.name,
            }
