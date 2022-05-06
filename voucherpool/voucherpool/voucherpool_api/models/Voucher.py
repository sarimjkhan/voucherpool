from django.db import models

from voucherpool_api.models.Customer import Customer
from voucherpool_api.models.SpecialOffer import SpecialOffer


class Voucher(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    expiry = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    specialOffer = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE, null=True)
    isUsed = models.BooleanField(default=False, null=False)
    dateConsumed = models.DateTimeField(default=None, null=True)

    def __str__(self) -> str:
        return self.code
