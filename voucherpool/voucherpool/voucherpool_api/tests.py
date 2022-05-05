from django.test import TestCase
from rest_framework.test import APITestCase
from .serializers import *
from .models import *

# Create your tests here.
class VoucherPoolTestCase(APITestCase):
    def getAllVouchers(self):
        response = self.client.get("api/vouchers")
        print("janicheck: ")
        print(response)
        self.assertEqual(response.status_code, 200)
