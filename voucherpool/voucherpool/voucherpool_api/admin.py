from django.contrib import admin
from .models import Customer, SpecialOffer, Voucher

# Register your models here.
admin.site.register(Customer)
admin.site.register(SpecialOffer)
admin.site.register(Voucher)
