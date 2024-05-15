from django.test import TestCase
from ..models import Customer, Retail


class CustomerTest(TestCase):
    """ Test module for Customer model"""


    def setUp(self):
        Customer.objects.create(
            customer_name="django test",
            payment_method="paypal",
        )

    def test_customer_info(self):
        customer = Customer.objects.get(customer_name='django test')
        self.assertEqual(
            customer.get_info(), "customer is django test and pays with paypal")

class RetailTest(TestCase):
    """Test module for retail model"""

    def setUp(self):
        Retail.objects.create(
            retail_name="Django Retail Test",
            accept_return=True,
            purchased_from = False,
        )
    
    def test_retail_info(self):
        retail = Retail.objects.get(retail_name="Django Retail Test")
        statement = "Django Retail Test: accepts return=True - purchased from=False"
        self.assertEqual(retail.get_info(), statement)