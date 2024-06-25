from django import forms
from .models import users,Company,ProductCompany,Category,SubCategory,Product,Distributor,Customer,Purchase

class StudentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    age = forms.IntegerField(label='Age')
    email = forms.EmailField(label='Email')
    

class UsersForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['id','fname','lname','age','email']
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['companyID','companyName','address','contactNo']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['CatID','CatName','PCID']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['id','name','CatID']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['CatID','CatName','PCID']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['PID','PName','image','CatID','PCoID','price','stock','details']
        
class ProductCompanyForm(forms.ModelForm):
    class Meta:
        model = ProductCompany
        fields = ['PCID','PCName','address','contactNo','email']

class DistributorForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = ['DID','DName','contactNo','email','companyID']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['id','name','email','address','phone']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['id','PCoID','DID','qty','totalBill','date']