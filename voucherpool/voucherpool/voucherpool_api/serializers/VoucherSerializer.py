from pyexpat import model
from rest_framework import serializers
from ..models import Voucher


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = "__all__"
        depth = 1
