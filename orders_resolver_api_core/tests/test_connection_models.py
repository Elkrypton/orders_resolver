from typing import Any
from ..serializers import *
from ..models import Customer, Retail
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status



#initiate the API Client
client = Client()

class TestCustomerConnection(TestCase):
    
    def setUp(self):
        Customer.objects.create(
            customer_name="rick sanchez",
            payment_method="cash",
        )

        Customer.objects.create(
            customer_name="richard mcallan",
            payment_method="cash",
        )
        Customer.objects.create(
            customer_name="king sanchez",
            payment_method="cash",
        )
    
    def test_get_all_customers(self):
        #get api response
        response = client.get(reverse('customer-list-create'))

        #get data from db
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)