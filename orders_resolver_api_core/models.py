from django.db import models

# Create your models here.

from django.db import models
import uuid
from time import time
from datetime import datetime, timedelta
from .constants import * 


# product_materials = [
# 	('PLASTIC','plastic'),
# 	('METAL','material'),
# 	('GLASS', 'glass'),
# 	('HYBRID', 'Hybrid'),
# ]

# area_of_use = [
# 	('HOUSE_01', 'Living Room'),
# 	('HOUSE_02', 'Kitchen'),
# 	('HOUSE_03', 'Bedroom'),
# 	('HOUSE_04', 'Bathroom'),
# ]

# product_categories = [('HOME DECOR', 'Home Decor'),
# 		      ('APPLIANCES', 'Appliances'),
# 			  ('ELECTRONICS', 'Electronics'),
# 			  ('ACCESSORIES', 'Accessories'),]


# DAMAGE_SOURCE = [
# 	('1001', 'customer damage'),
# 	('1002', 'vendor damage'),
# 	('1003',  'retail damage'),
# 	('0000',  None),
# ]

# ISSUE_TYPES = [
#  ('DEFECTIVE', 'defective unit'),
#  ('WRONG UNIT', 'wrong unit'),
#  ('OTHER', 'other reason'),

# ]

# DELIVERY_STATUS = [
# 	('Preparing for shippment', '0001'),
# 	('SHIPPED', '0002'),
# 	('OUT FOR DELIVERY', '0003'),
# 	('DELIVERED', '0004'),
# ]

# ISSUE_STATUS = [
# 	('0001', 'failed'),
# 	('0000', 'processing'),
# 	('0002', 'passed'),
# ]

# PAYMENT_METHODS = [('card','credit/debit'),
# 		   			('cash', 'cash'),
# 	 				('paypal', 'paypal')]

# PURCHASE_LOCATION = [('store', 'store'),
# 		      	('online', 'online'),
# 				('VENDOR','Vendor Direct')]


# This Python class defines a Link model representing transactions between a Retail entity, a Vendor
# entity, and a Customer entity, with a method to generate a unique transaction ID.
class Link(models.Model):

	"""
	Link Model to represent transaction between Retail, Vendor and Customer
	Attributes:

	relation_A = Foreignkey to Retail Instance
	relatoion_B = Foreignkey to Vendor Instance
	customer = Foreignkey to Customer Instance

	"""
	link_id = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	relation_A = models.ForeignKey('Retail', on_delete=models.CASCADE)
	relation_B = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
	
	def generate_transaction_id(self):
		prefix="RE"
		random_part = str(uuid.uuid4().int)[:8]
		sequential_part = str(uuid.uuid4().int)[:10]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):
		if not self.link_id:
			self.link_id = self.generate_transaction_id()
		super(Link, self).save(*args, **kwargs)
	

	def __str__(self):
		return f"{self.link_id}: {self.relation_A} AND {self.relation_B}"
	

# The `Product` class in the Python code defines a model with various fields for product information
# and includes methods for generating a unique product ID and handling warranty status.
class Product(models.Model):


	product_id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False)
	product = models.CharField(max_length=100)
	model_n = models.CharField(max_length=100, blank=True, null=True)
	serial_n = models.CharField(max_length=100, blank=True, null=True, unique=True)
	returnable = models.BooleanField(default=False)
	product_materials = models.CharField(max_length=255, choices=product_materials)
	product_categories = models.CharField(max_length=255, choices=product_categories)
	product_area_of_use = models.CharField(max_length=255, choices=area_of_use)
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
	active_warranty = models.BooleanField(default=True)
	owned_before = models.BooleanField(default=False)
	

	def generate_product_id(self):
		prefix = "PROD"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"

	
	def save(self, *args, **kwargs):
		if not self.product_id:
			self.product_id = self.generate_product_id()
		
		if self.owned_before:
			self.active_warranty = False
		
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return f"Product : {self.product} - Returnable : {self.returnable}"

class Issue(models.Model):
	issue_id = models.CharField(max_length=255, primary_key=True, editable=False, unique=True)
	issue_initiated = models.BooleanField(default=False)
	issue_status = models.CharField(choices=ISSUE_STATUS, max_length=100)
	order_issued = models.ForeignKey('Order', on_delete=models.CASCADE)
	link = models.ForeignKey('Link', on_delete=models.CASCADE, null=True)
	

	def generate_issue_id(self):
		prefix = "ISS"
		random_part = str(uuid.uuid4().int)[:6]
		sequential_part = str(uuid.uuid4().int)[:7]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):
		if not self.issue_id:
			self.issue_id = self.generate_issue_id()
		super(Issue, self).save(*args, **kwargs)

	def __str__(self):
		return f"Issue : {self.issue_status}"


class Retail(models.Model):

	"""Retail model 

	Returns:
		__str__() ->: Retail instance primary key: 
	"""


	retail_id = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	retail_name = models.CharField(max_length=100, unique='True')
	accept_return = models.BooleanField(default=False)
	return_to_warehouse_window = models.IntegerField(default=48, editable=False)
	return_to_store_window = models.IntegerField(default=2160, editable=False)
	purchased_from = models.BooleanField(default=False)
	products_purchased = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)

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
	vendor_name = models.CharField(max_length=100, unique=True)
	accept_return = models.BooleanField(default=False)
	return_window = models.IntegerField(default=720, editable=False)
	related_retails = models.ForeignKey('Retail', on_delete=models.CASCADE, null=True)

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

class Delivery(models.Model):

	"""
	Delivery Class Model 
	Attributes:
		related_order : 90Foreign key(Order number)
		delivery_status : Tuples of Choices
		date_delivered: Manually added (auto added as well()
		issue: Foreign Key for related issue instances
	"""

	delivery_id = models.CharField(max_length=255, primary_key=True, unique=True)
	related_order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
	delivery_status = models.CharField(max_length=233, choices=DELIVERY_STATUS)
	date_delivered = models.DateTimeField(auto_now_add=False)
	issue = models.ForeignKey('Issue', on_delete=models.CASCADE, null=True)


	def generate_delivery_id(self):
		prefix = "DEL"
		random_part = str(uuid.uuid4().int)[:10]
		sequential_part = str(uuid.uuid4().int)[:7]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):

		if self.delivery_status == "DELIVERED":
			self.date_delivered = datetime.now()
		super(Delivery, self).save(*args, **kwargs)
	
	def __str__(self):
		return f"{self.delivery_status}"
	
	def __doc__(self):
		return Delivery.__doc__()
		


class Order(models.Model):

	order_number = models.CharField(max_length=255, unique=True, editable=False, primary_key=True)
	product = models.ForeignKey('Product',on_delete=models.CASCADE, null=True, blank=True)
	retail = models.ForeignKey('Retail', on_delete=models.CASCADE, null=True, blank=True)
	vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, blank=True, null=True)
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, null=True)
	order_location = models.CharField(choices=PURCHASE_LOCATION, max_length=100)
	damage = models.CharField(max_length=255, choices=DAMAGE_SOURCE, default=False, null=True)
	delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS)
	link = models.ForeignKey('Link', on_delete=models.CASCADE, null=True)
	date_delivered = models.DateTimeField((""), auto_now=False, auto_now_add=False)
	ordered = models.BooleanField(default=False)
	

	def generate_order_number(self):
		prefix = "IR"
		random_part = str(uuid.uuid4().int)[:5]
		sequential_part = str(uuid.uuid4().int)[:5]
		return f"{prefix}-{random_part}-{sequential_part}"
	
	def save(self, *args, **kwargs):

		if not self.pk:
			link = Link.objects.create(
				relation_A = self.retail,
				relation_B = self.vendor,
				customer = self.customer
			)
			self.link = link

		if not self.order_number and self.ordered == True:
			self.order_number = self.generate_order_number()

		if self.delivery_status != 'Delivered':
			self.damage = None
		
		if self.delivery_status == 'DELIVERED':
			self.date_delivered = str(datetime.datetime.today())

		super(Order, self).save(*args, **kwargs)

	def __str__(self):
		return f"Order Number : {self.order_number}-'\
				{self.retail}-{self.vendor}"

