from django.db import models
from django.conf import settings

# Create your models here.

class users(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=255)
    
class Company(models.Model):
    companyID = models.IntegerField(primary_key=True)
    companyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contactNo = models.IntegerField()

class ProductCompany(models.Model):
    PCID = models.IntegerField(primary_key=True)
    PCName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contactNo = models.IntegerField()
    email = models.CharField(max_length=255)
    
class Category(models.Model):
    CatID = models.IntegerField(primary_key=True)
    CatName = models.CharField(max_length=255)
    PCID = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    @property
    def CompanyName(self):
        return self.PCID.companyName

class SubCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    CatID = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    @property
    def CategoryName(self):
        return self.CatID.CatName
    
class Product(models.Model):
    PID = models.IntegerField(primary_key=True)
    PName = models.CharField(max_length=255)
    image = models.FileField(upload_to=settings.BASE_DIR/"myapp/media",max_length=255,null=True)
    CatID = models.ForeignKey(Category,on_delete=models.CASCADE)
    PCoID = models.ForeignKey(ProductCompany,on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.CharField(max_length=11)
    details = models.CharField(max_length=255)

    @property
    def CategoryName(self):
        return self.CatID.CatName
    
    @property
    def ProductCompanyName(self):
        return self.PCoID.PCName
    
class Distributor(models.Model):
    DID = models.IntegerField(primary_key=True)
    DName  =models.CharField(max_length=255)
    contactNo = models.IntegerField()
    email = models.CharField(max_length=255)
    companyID = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    @property
    def CompanyName(self):
        return self.companyID.companyName

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Purchase(models.Model):
    id = models.IntegerField(primary_key=True)
    PCoID  =models.ForeignKey(ProductCompany,on_delete=models.CASCADE)
    DID  =models.ForeignKey(Distributor,on_delete=models.CASCADE)
    qty = models.IntegerField()
    totalBill = models.IntegerField()
    date = models.DateField()
    
    @property
    def CompanyName(self):
        return self.PCoID.PCName

    @property
    def DistributorName(self):
        return self.DID.DName
    