from rest_framework import viewsets
from ..models import Customer, SpecialOffer
from ..serializers import SpecialOfferSerializer


class SpecialOfferApiView(viewsets.ModelViewSet):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
