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
	lookup_field = 'pk'
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

    def __init__(self, delivery_status ,retail_name=None, vendor_name=None):
        self.retail_name = retail_name
        self.vendor_name = vendor_name
        self.delivery_status = delivery_status

    def check_all_conditions(self):
        try:
            order = Order.objects.all()
            retail = Retail.objects.get(retail_name=self.retail_name)
            vendor = Vendor.objects.get(vendor_name=self.vendor_name)
            products = Product.objects.filter(returnable=True)
	    

            for product in products:
                if (retail.accept_return and vendor.accept_return and
                        ((retail.return_to_warehouse_window == 48 and order.damage == 'vendor_damage') or
                         (vendor.return_window == 720 and vendor.vendor_error) or
                         (retail.return_to_store_window == 720 and vendor.vendor_error))):
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
        except (Retail.DoesNotExist, Vendor.DoesNotExist) as e:
            return f"Retail or Vendor not found: {e}"
	
def initiate_return_case(request, order_number):
	retail_name = Retail.objects.all()
	vendor_name = Vendor.objects.all()
	order = Order.objects.get(order_number=str(order_number))
	if order.delivery_status == '0004':
	    return_case = InitiateReturnCase(retail_name, vendor_name)
	    result = return_case.check_all_conditions()
	    return JsonResponse({'result': result})
	else:
		return JsonResponse({'result': "return Case cannot be initiated when unit has not been delivererd yet."})