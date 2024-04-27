from django.contrib import admin

# Register your models hererom .models import *


from .models import *

admin.register(Order)
admin.register(Product)
admin.register(Vendor)
admin.register(Retail)
admin.register(Issue)
admin.register(Customer)

