from datetime import datetime
import string
import random
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from ..models import Customer, Voucher
from ..serializers import VoucherSerializer


class VoucherApiView(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    # (1)Generate Voucher Code for each customer for a given Special Offer and expiration data
    @api_view(["GET"])
    def generate(self, specialOfferId=None):
        customers = Customer.objects.all()
        for customer in customers:
            code = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
            voucher = Voucher(
                code=code,
                customer_id=customer.id,
                specialOffer_id=specialOfferId,
                isUsed=False,
            )
            voucher.save()

        return Response({"status": 200, "result": "success"})

    # (2)Provide an endpoint, reachable via HTTP, which receives a Voucher Code and Email and validates the Voucher Code.
    # In Case it is valid, return the Percentage Discount and set the date of usage.
    @api_view(["GET"])
    def validateCode(self, code, email):
        try:
            customer = Customer.objects.get(email=email)
            voucher = Voucher.objects.get(
                code=code, customer_id=customer.id, isUsed=False
            )
        except:
            return Response(
                {
                    "status": 400,
                    "result": "error",
                    "message": "Unable to find relevant customer/voucher",
                }
            )
        else:
            voucher.dateConsumed = datetime.now()
            voucher.isUsed = True
            voucher.save(update_fields=["dateConsumed"])
            return Response(
                {
                    "status": 200,
                    "result": "success",
                    "message": "Voucher has been validated",
                    "data": {"discount": voucher.specialOffer.discount},
                }
            )

    # (3)For a given Email return all its valid Voucher Codes with the Name of the Special Offer
    @api_view(["GET"])
    def getCodes(self, email=None):
        customer = Customer.objects.get(email=email)
        vouchers = Voucher.objects.filter(customer_id=customer.id, isUsed=False)

        voucherSerializer = VoucherSerializer(vouchers, many=True)
        return Response(voucherSerializer.data)
