from django.contrib import admin

# Register your models here.
from .models import *

class ImagesTublerinline(admin.TabularInline):
    model = Images

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinline]


class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]
    list_display = ['firstname','email','payment_id','paid','date']
    search_fields = ['firstname','email','payment_id']


admin.site.register(Images)

admin.site.register(Categories)

admin.site.register(Product,ProductAdmin)
admin.site.register(Contact_us)

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)



