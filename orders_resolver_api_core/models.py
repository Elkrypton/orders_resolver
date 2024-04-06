from django.db import models

# Create your models here.

from django.db import models
import uuid

from time import time


product_materials = [
	('PLASTIC','plastic'),
	('METAL','material'),
	('GLASS', 'glass'),
]

product_categories = [('HOME DECOR', 'Home Decor'),
		      ('APPLIANCES', 'Appliances'),
			  ('ELECTRONICS', 'Electronics'),
			  ('ACCESSORIES', 'Accessories'),]



DAMAGE_SOURCE = [
	('1001', 'customer damage'),
	('1002', 'vendor damage'),
	('1003',  'retail damage'),
	('0000',  None),
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
	product_id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
	ordered = models.BooleanField(default=False, blank=True, null=True)
	product = models.CharField(max_length=100)
	returnable = models.BooleanField(default=False)
	product_materials = models.CharField(max_length=255, choices=product_materials)
	product_categories = models.CharField(max_length=255, choices=product_categories)

	def generate_product_id(self):
		prefix = "PROD"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"

	
	def save(self, *args, **kwargs):
		if not self.product_id:
			self.product_id = self.generate_product_id()
		
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return f"Product : {self.product} - Returnable : {self.returnable}"

class Issue(models.Model):
	issue_id = models.CharField(max_length=255, null=True, blank=True)
	issue_initiated = models.BooleanField(default=False)
	issue_status = models.CharField(choices=ISSUE_STATUS, max_length=100)

	def __str__(self):
		return f"Issue : {self.issue_status}"


class Retail(models.Model):
	retail_id = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	retail_name = models.CharField(max_length=100)
	accept_return = models.BooleanField(default=False)
	return_to_warehouse_window = models.IntegerField(default=48, editable=False)
	return_to_store_window = models.IntegerField(default=2160, editable=False)
	purchased_from = models.BooleanField(default=False)

	def generate_retail_id(self):
		prefix = "RET"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args,**kwargs):
		if not self.retail_id:
			self.retail_id = self.generate_retail_id()
		
		super(Retail, self).save(*args, **kwargs)


	def __str__(self):
		return f"Retail Name : {self.retail_name}"


class Vendor(models.Model):
	vendor_id = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	vendor_name = models.CharField(max_length=100)
	accept_return = models.BooleanField(default=False)
	return_window = models.CharField(default=720, editable=False, max_length=100)

	def generate_vendor_id(self):
		prefix = "VEND"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args,**kwargs):
		if not self.vendor_id:
			self.vendor_id = self.generate_vendor_id()
		
		super(Vendor, self).save(*args, **kwargs)

	def __str__(self):
		return f"Vendor Name : {self.vendor_name} - {self.vendor_id}"
	
class Customer(models.Model):
	customer_id = models.CharField(max_length=255, editable=False, unique=True, primary_key=True)
	customer_name = models.CharField(max_length=100)
	payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=100)
	purchased_from = models.ForeignKey('Retail', on_delete=models.CASCADE, null=True)
	products_purchased = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
	

	def generate_customer_id(self):
		prefix = "CUST"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"

	def save(self, *args, **kwargs):
		if not self.customer_id:
			self.customer_id = self.generate_customer_id()
		super(Customer, self).save(*args, **kwargs)

	def __str__(self):
		return f"Customer ID : {self.customer_id}"


class Order(models.Model):

	order_number = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
	retail = models.ForeignKey('Retail', on_delete=models.CASCADE, null=True, blank=True)
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True)
	order_location = models.CharField(choices=PURCHASE_LOCATION, max_length=100)
	delivery_status = models.CharField(max_length=233, choices=DELIVERY_STATUS)
	damage = models.CharField(max_length=255, choices=DAMAGE_SOURCE, default=False, null=True)
	issues = models.ForeignKey('Issue', on_delete=models.CASCADE,  null=True, default=None)

	def generate_order_number(self):
		prefix = "IR"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):

		if not self.order_number:
			self.order_number = self.generate_order_number()

		if self.delivery_status != 'DELIVERED':
			self.damage = None
		super(Order, self).save(*args, **kwargs)

	def __str__(self):
		return f"Order Number : {self.order_number}"
	

