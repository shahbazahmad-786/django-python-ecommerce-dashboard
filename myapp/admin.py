from django.contrib import admin
from .models import users,Company,Category,SubCategory,Product,ProductCompany,Distributor,Customer,Purchase

# Register your models here.
admin.site.register(users)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductCompany)
admin.site.register(Distributor)
admin.site.register(Customer)
admin.site.register(Purchase)
