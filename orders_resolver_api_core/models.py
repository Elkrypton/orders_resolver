from django.db import models

# Create your models here.

from django.db import models
import uuid

from time import time


DAMAGE_SOURCE = [
	('CUSTOMER_DAMAGE', 'customer damage'),
	('VENDOR_DAMAGE', 'vendor damage'),
	('RETAIL_DAMAGE',  'retail damage'),
]

ISSUE_TYPES = [
 ('DEFECTIVE', 'defective unit'),
 ('WRONG UNIT', 'wrong unit'),
 ('OTHER', 'other reason'),

]

DELIVERY_STATUS = [
	('Preparing for shippment', '0001'),
	('SHIPPED', '0002'),
	('OUT FOR DELIVERY', '0003'),
	('DELIVERED', '0004'),
]

ISSUE_STATUS = [
	('ISSUED', 'failed'),
	('PROCESSING', 'processing'),
	('PASSED', 'passed'),
	('FAILED', 'failed'),
]

PAYMENT_METHODS = [('card','credit/debit'),
		   			('cash', 'cash'),
	 				('paypal', 'paypal')]

PURCHASE_LOCATION = [('store', 'store'),
		      	('online', 'online'),
				('VENDOR','Vendor Direct')]

class Product(models.Model):
	product = models.CharField(max_length=100)
	returnable = models.BooleanField(default=False)
	
	def __str__(self):
		return f"Product : {self.product}"


class Issue(models.Model):
	issue_id = models.CharField(max_length=255, null=True, blank=True)
	issue_initiated = models.BooleanField(default=False)
	issue_status = models.CharField(choices=ISSUE_STATUS, max_length=100)

	def __str__(self):
		return f"Issue : {self.issue_status}"


class Retail(models.Model):
	retail_name = models.CharField(max_length=100)
	accept_return = models.BooleanField(default=False)
	return_to_warehouse_window = models.IntegerField(default=48, editable=False)
	return_to_store_window = models.IntegerField(default=2160, editable=False)

	def __str__(self):
		return f"Retail Name : {self.retail_name}"

class Vendor(models.Model):
	vendor_name = models.CharField(max_length=100)
	accept_return = models.BooleanField(default=False)
	return_window = models.CharField(default=720, editable=False, max_length=100)


	def __str__(self):
		return f"Vendor Name : {self.vendor_name}"
	
class Customer(models.Model):
	customer_name = models.CharField(max_length=100)
	payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=100)

	def __str__(self):
		return f"Customer Name : {self.customer_name}"


class Order(models.Model):
	order_number = models.CharField(max_length=255)
	product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
	retail = models.ForeignKey('Retail', on_delete=models.CASCADE, null=True, blank=True)
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True)
	order_location = models.CharField(choices=PURCHASE_LOCATION, max_length=100)
	delivery_status = models.CharField(max_length=233, choices=DELIVERY_STATUS)
	damage = models.CharField(max_length=255, choices=DAMAGE_SOURCE)


	def generate_order_number(self):
		prefix = "IR"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):
		if not self.order_number:
			self.order_number = self.generate_order_number()

	
	def __str__(self):
		return f"Order Number : {self.order_number}"
	


