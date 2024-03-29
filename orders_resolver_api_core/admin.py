from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Retail)
admin.site.register(Customer)
admin.site.register(Product)