from pyexpat import model
from rest_framework import serializers
from ..models import SpecialOffer


class SpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOffer
        fields = ["name", "discount"]
