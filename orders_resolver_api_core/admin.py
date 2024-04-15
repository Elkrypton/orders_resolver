from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from django.contrib import admin
from .models import *


admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(Retail)
admin.site.register(Customer)
admin.site.register(Product)
=======
from .models import *


admin.register(Order)
admin.register(Product)
admin.register(Vendor)
admin.register(Retail)
admin.register(Issue)
admin.register(Customer)
>>>>>>> refs/remotes/origin/master
