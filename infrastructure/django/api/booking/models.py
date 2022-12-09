import uuid
from django.db import models
from customers.models import Customer


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checkin = models.DateField(auto_now=False)
    checkout = models.DateField(auto_now=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
