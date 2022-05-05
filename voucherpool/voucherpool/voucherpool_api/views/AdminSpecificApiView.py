from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from ..models import Customer, Voucher
from ..serializers import VoucherSerializer


class AdminSpecificApiView(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    # (4)search voucher by email (admin only)
    @api_view(["GET"])
    @permission_classes([IsAdminUser])
    def getCodesForAdmin(self):
        email = self.query_params.get("email")
        customer = Customer.objects.get(email=email)
        vouchers = Voucher.objects.filter(customer_id=customer.id)

        voucherSerializer = VoucherSerializer(vouchers, many=True)
        return Response(voucherSerializer.data)
