from django.shortcuts import render
from rest_framework import generics
from .models import (
Order, Product, Issue, Vendor, Retail, Customer)
from .serializers import *
from django.http import JsonResponse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.
import uuid

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = OrderSerializer
	lookup_field = 'order_number'
	def get_queryset(self):
		return Order.objects.all()


# class DamageAPIView(generics.ListCreateAPIView):
# 	queryset = Damage.objects.all()
# 	serializer_class = DamageSerializer
	
# class DeliveryAPIView(generics.ListCreateAPIView):
# 	queryset = Delivery.objects.all()
# 	serializer_class = DeliverySerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class IssueListCreateAPIView(generics.ListCreateAPIView):
	queryset = Issue.objects.all()
	lookup_field = "order_number"
	serializer_class = IssueSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
	queryset = Vendor.objects.all()
	serializer_class = VendorSerializer

class RetailListCreateAPIView(generics.ListCreateAPIView):
	queryset = Retail.objects.all()
	serializer_class = RetailSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer


def generate_random_issue_id():
	prefix = "IS"
	random_part = str(uuid.uuid4().int)[:5]
	sequential_part = str(uuid.uuid4().int)[:5]
	return f"{prefix}-{random_part}-{sequential_part}"
	

class InitiateReturnCase:

    def __init__(self, order):
        self.order = order
        self.retail = order.retail
        self.vendor = order.vendor
        self.delivery_status = order.delivery_status
        self.product = order.product

    def check_all_conditions(self):
	    
        if self.product.returnable:
                if (self.retail.accept_return and self.vendor.accept_return and
                        ((self.retail.return_to_warehouse_window == 48 and self.order.damage == '1002') or
                         (self.vendor.return_window == 720 and self.order.damage=="1002") or
                         (self.retail.return_to_store_window == 720 and self.order.damage== "1003"))):
                    issue = Issue.objects.create(
                        issue_id=generate_random_issue_id(),
                        issue_initiated=True,
                        issue_status='passed'
                    )
                    issue.save()
                else:
                    issue = Issue.objects.create(
                        issue_id=generate_random_issue_id(),
                        issue_initiated=True,
                        issue_status='failed'
                    )
                    issue.save()

        return str(issue)
	
def initiate_return_case(request, order_number):
	
	order = Order.objects.get(order_number=order_number)
	print(order)
	if order.delivery_status == 'DELIVERED':
	    return_case = InitiateReturnCase(order)
	    result = return_case.check_all_conditions()
	    return JsonResponse({'result': result})

	else:
		return JsonResponse({'result': "return Case cannot be initiated when unit has not been delivererd yet."})