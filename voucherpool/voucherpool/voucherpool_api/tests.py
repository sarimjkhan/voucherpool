from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from .serializers import *
from .models import *

# Very simple unit test cases for specifically get calls
class VoucherPoolTestCase(APITestCase):
    def test_getAllVouchers(self):
        response = self.client.get('http://localhost:8000/api/vouchers/', format='json')
        assert response.status_code, 200

    def test_getSingleVoucher(self):
        response = self.client.get('http://localhost:8000/api/vouchers/1/', format='json')
        assert response.status_code, 200

    def test_deleteVoucher(self):
        response = self.client.delete("http://localhost:8000/api/vouchers/1", format='json')
        assert response.status_code, 200
    
    def test_getAllCustomers(self):
        response = self.client.get('http://localhost:8000/api/customers/', format='json')
        assert response.status_code, 200

    def test_getSingleCustomer(self):
        response = self.client.get('http://localhost:8000/api/customers/1/', format='json')
        assert response.status_code, 200

    def test_deleteCustomer(self):
        response = self.client.delete("http://localhost:8000/api/customers/1", format='json')
        assert response.status_code, 200

    def test_getAllSpecialOffers(self):
        response = self.client.get('http://localhost:8000/api/specialoffers/', format='json')
        assert response.status_code, 200

    def test_getSingleSpecialOffers(self):
        response = self.client.get('http://localhost:8000/api/specialoffers/2/', format='json')
        assert response.status_code, 200

    def test_deleteSpecialOffers(self):
        response = self.client.delete("http://localhost:8000/api/specialoffers/2", format='json')
        assert response.status_code, 200

    def test_generateCodes(self):
        response = self.client.get("http://localhost:8000/api/vouchers/generate/2", format='json')
        assert response.status_code, 200

    def test_validateCode(self):
        response = self.client.get("http://localhost:8000/api/vouchers/validatecode/WQDX741O/rehan@jalil.com", format='json')
        assert response.status_code, 200

    def test_getCodesByEmail(self):
        response = self.client.get("http://localhost:8000/api/vouchers/codes/rehan@jalil.com/", format='json')
        assert response.status_code, 200
    