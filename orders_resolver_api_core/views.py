from django.core.cache import cache
import redis
import time
from rest_framework.response import Response
from datetime import timedelta, datetime
from rest_framework import generics, mixins
from .models import (
Order, Product, Issue, Vendor, Retail, Customer, Delivery, Link)
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.

# The line `redis_instance = redis.StrictRedis(host="127.0.0.1", port=637, db=1)` is creating an
# instance of a Redis client using the `StrictRedis` class from the `redis` library in Python.
redis_instance = redis.StrictRedis(host="127.0.0.1", port=637, db=1)



# The CachedAPIViewMixin class provides a method for caching API responses using Redis.
class CachedAPIViewMixin:
	cache_timeout = 40*40

	def cached_response(self, cache_key, queryset,  serializer_class):
		if cache_key in cache:
			print(">>> REDIS ....")
			cached_data = cache.get(cache_key)
			return Response(cached_data)
		else:
			print(">>> DB RESPONE... ")
			serializer_instance = serializer_class(queryset, many=True)
			cached_data = serializer_instance.data
			cache.set(cache_key, cached_data, timeout=self.cache_timeout)
			return Response(cached_data)
		
def log_db_queries(f):
	"""
	The `log_db_queries` function is a Python decorator that logs database queries executed by a
	function along with their execution time.
	
	:param f: The `f` parameter in the `log_db_queries` function is a function that you want to decorate
	with additional functionality to log database queries. This function will be called with the same
	arguments and keyword arguments as the original function
	:return: The `log_db_queries` function is a decorator that wraps another function `f` and adds
	logging functionality for database queries executed by `f`. The decorator prints out the total count
	of queries, the time taken for each query, the SQL query itself, and the total time taken for all
	queries to execute. The original function `f` is then called and its result is returned.
	"""
	from django.db import connection
	def  new_f(*args, **kwargs):
		start_time = time.time()
		res = f(*args, **kwargs)
		print("\n\n")
		print("-"*80)
		print("db queries log for :{}\n".format(f.__name__))
		print("TOTAL COUNT : {}".format(len(connection.queries)))
		for q in connection.queries:
			print("{} : {}\n".format(q["time"], q["sql"]))
		
		end_time = time.time()
		duration = end_time - start_time
		print("\n Total Time: {:.3f} ms".format(duration * 1000.0))
		print("-" *80)
		return res
	return new_f





# This class is an API view in Django REST framework for listing and creating Order objects, with
# caching and logging of database queries.
class OrderList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, CachedAPIViewMixin):
	serializer_class = OrderSerializer
	queryset = Order.objects.all()
	
	@log_db_queries
	def get(self,request, *args, **kwargs):
		pk = self.request.query_params.get('order_number')
		if pk is not None:
			cache_key = 'order_number' +  pk
		else:
			cache_key = 'order_number'
		
		queryset = Order.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		return self.cached_response(cache_key, queryset, self.serializer_class)
	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


# This class is an API view in Django REST framework for retrieving, updating, and deleting order
# details, with caching implemented for improved performance.
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView, CachedAPIViewMixin):
	serializer_class = OrderSerializer
	lookup_field = 'order_number'
	def get_queryset(self):
		return Order.objects.all()
	
	def get(self, request, *args, **kwargs):
		pk = self.request.query_params.get('order_number')
		if pk is not None:
			cache_key = 'order_id' + pk
		
		else:
			cache_key = 'order_id'
		
		queryset = Order.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		return self.cached_response(cache_key,  queryset, self.serializer_class)
	

# This class is a Django REST framework view for retrieving, updating, and deleting product details
# with caching functionality.
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProductSerializer
	lookup_field = 'product_id'
	def get_queryset(self):
		return Product.objects.all()
	
	@log_db_queries
	def list(self, request, *args, **kwargs):
		pk = self.request.query_params.get('pk')
		if pk is not None:
			cache_key = 'product_id' + pk
		
		else:
			cache_key = 'product_id'
		
		queryset = Product.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)

			 

# The `RelationshipAPIView` class is a Django REST framework view that lists and creates instances of
# the `Link` model, with caching and logging of database queries implemented.
class RelationshipAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Link.objects.all()
	serializer_class = RelationshipSerializer
	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('pk')
		if pk is not None:
			cache_key = 'link' + pk
		else:
			cache_key = 'link'
		queryset = Link.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
	
		return self.cached_response(cache_key, queryset, self.serializer_class)

# class DamageAPIView(generics.ListCreateAPIView):
# 	queryset = Damage.objects.all()
# 	serializer_class = DamageSerializer
	
class DeliveryAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Delivery.objects.all()
	serializer_class = DeliverySerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('delivery_id')
		if pk is not None:
			cache_key = 'delivery' + pk

		else:
			cache_key = 'delivery'
		queryset = Delivery.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)


class OrderListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	serializer_class = OrderSerializer
	lookup_field = "pk"
	def get_queryset(self):
		return Order.objects.all()

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('order_number')
		if pk is not None:
			cache_key = 'order_number' + pk
		
		else:
			cache_key = 'order_number'
		
		queryset  = Order.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)

		
	
# This class is a ListCreateAPIView for products with caching and logging of database queries.
class ProductListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('product_id')
		if pk is not None:
			cache_key = 'product_id' + pk
		else:
			cache_key = 'product_id'
		queryset = Product.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)
			
		

# This class is a Django API view that lists and creates instances of the Issue model, with caching
# and logging of database queries.

class IssueListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Issue.objects.all()
	lookup_field = "pk"
	serializer_class = IssueSerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('order_number')
		if pk is not None:
			cache_key = 'issue_id' + pk
		else:
			cache_key = 'issue_id'
		queryset = Issue.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)


# The above code defines two API views for listing and creating Vendor and Retail objects, with
# caching and logging of database queries implemented.
class VendorListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('pk')
		if pk is not None:
			cache_key = 'vendor_id' + pk
		else:
			cache_key = 'vendor_id'
		queryset = Vendor.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)
# The `RetailListCreateAPIView` class is a Django REST framework view that handles listing and
# creating `Retail` objects, with caching and logging of database queries.

class RetailListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Retail.objects.all()
	serializer_class = RetailSerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('pk')
		if pk is not None:
			cache_key = 'retail_id' + pk
		else:
			cache_key = 'retail_id'
		queryset = Retail.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)
# This class is a Django REST framework API view for listing and creating Customer objects, with
# caching and logging of database queries.


class CustomerListCreateAPIView(generics.ListCreateAPIView, CachedAPIViewMixin):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

	@log_db_queries
	def list(self, request):
		pk = self.request.query_params.get('pk')
		if pk is not None:
			cache_key = 'customer_id' + pk
		else:
			cache_key = 'customer_id'
		queryset = Customer.objects.all()
		if pk:
			queryset = queryset.filter(pk=pk)
		
		return self.cached_response(cache_key, queryset, self.serializer_class)


def initiate_return_case(request, order_number):
	"""
	This Python function initiates a return case for a given order if the delivery status is
	'Delivered'.
	
	:param request: The `request` parameter in the `initiate_return_case` function is typically an
	HttpRequest object that represents the current HTTP request. It contains metadata about the request,
	such as headers, method, and user data. This parameter allows you to access information about the
	incoming request and process it accordingly within the
	:param order_number: The `initiate_return_case` function takes two parameters: `request` and
	`order_number`. The `order_number` parameter is used to identify the specific order for which the
	return case is being initiated. It is passed to the function to retrieve the order details from the
	database using the `get
	:return: The code snippet provided is a Python function `initiate_return_case` that takes two
	parameters `request` and `order_number`.
	"""
	
	order = get_object_or_404(Order, order_number=order_number)
	print(order)
	if order.delivery_status == 'Delivered':
	    return_case = InitiateReturnCase(order)
	    result = return_case.check_all_conditions()
	    return JsonResponse({'result': result})

	else:
		return JsonResponse({'result': "return Case cannot be initiated when unit has not been delivererd yet."})

# The `InitiateReturnCase` class in Python checks conditions for initiating a return based on product
# returnability, acceptance by retail and vendor, and time window for return.
class InitiateReturnCase:
	def __init__(self, order):
		self.order = order
		self.retail = order.retail
		self.vendor = order.vendor
		self.delivery_status = order.delivery_status
		self.product = order.product
		self.issue_state = False
		
	def check_all_conditions(self):
		
		order_instance = Order.objects.get(order_number=self.order_number)
			
		if not self.product.returnable:
			self.issue_state = False
			return f"{self.product.product} is not returnable!"
		
		if not (self.retail.accept_return and self.vendor.accept_return):
			self.issue_state = False
			Issue.objects.create(
				issue_initiated=True,
				issue_status='Failed',
				order_issued=order_instance,
				link = self.order.link_id,

			)
			return f"{self.retail.retail_name} and {self.vendor.vendor_name} do not accept return"
		
		current_time = datetime.now().replace(tzinfo=None) #make current time naive
		delivery_time = self.order.date_delivered.replace(tzinfo=None)
		time_difference = current_time - delivery_time

		if time_difference <= timedelta(hours=self.vendor.return_window):
			self.issue_state = True
			Issue.objects.create(
				issue_initiated=True,
				issue_status='Passed',
				order_issued=self.order.order_number,
				link = self.order.link_id,

			)
			return f"Passed : Return initiated within vendor's return window"
		
		if time_difference <= timedelta(days=90):
			self.issue_state = True
			Issue.objects.create(
				issue_initiated=True,
				issue_status='Passed',
				order_issued=self.order.order_number,
				link = self.order.link_id,

			)
			return f"Passed :Return initiated wirthin retailer's return window"
			
		else:
			self.issue_state = False
			return f"Failed :Return of the unit failed either to the warehouse "
		
		


    


