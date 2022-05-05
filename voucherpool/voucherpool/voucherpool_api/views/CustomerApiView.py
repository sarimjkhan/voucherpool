from datetime import datetime
from rest_framework import viewsets
from ..models import Customer
from ..serializers import CustomerSerializer


class CustomerApiView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
