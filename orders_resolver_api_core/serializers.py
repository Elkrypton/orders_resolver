from rest_framework import serializers
from .models import (
    Order, 
    Product, 
    Issue,
    Customer,
    Vendor,
    Retail,
    # Damage,
     Delivery, 
    Link
)

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = "__all__"

class RelationshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Link
		fields = "__all__"
	

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"

class IssueSerializer(serializers.ModelSerializer):
	class Meta:
		model = Issue
		fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = "__all__"

class VendorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vendor
		fields = "__all__"

class RetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Retail
		fields = "__all__"

# class DamageSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Damage
# 		fields = "__all__"

class DeliverySerializer(serializers.ModelSerializer):
	class Meta:
		model = Delivery
		fields = "__all__"
	