
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerListCreateAPIView,
    OrderListCreateAPIView, 
    ProductListCreateAPIView,
    IssueListCreateAPIView,
    VendorListCreateAPIView,
    RetailListCreateAPIView,
    OrderDetailAPIView, 
    InitiateReturnCase,
    initiate_return_case,
    # DamageAPIView,
    DeliveryAPIView,
    RelationshipAPIView,
)

urlpatterns = [
    	path('', OrderListCreateAPIView.as_view(), name='order-list-create'),
		path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
        path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
        path('issue/', IssueListCreateAPIView.as_view(), name='issue-list-create'),
        path('customer/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
        path('vendor/', VendorListCreateAPIView.as_view(), name='vendor-list-create'),
        path('delivery/', DeliveryAPIView.as_view(), name='delivery-list-create'),
        path('relationship/', RelationshipAPIView.as_view(), name='relation-list-create'),
        path('retail/', RetailListCreateAPIView.as_view(), name='retail-list-create'),
        path('order-details/<order_number>/', OrderDetailAPIView.as_view(), name='order-detail-create'),
        path('issue/initiate_return/<order_number>/',initiate_return_case, name="initiate-return-case"),
        # path('delivery/', DeliveryAPIView.as_view(), name='delivery_status'),
        # path('damage/', DamageAPIView.as_view(), name='damage'),

	]
