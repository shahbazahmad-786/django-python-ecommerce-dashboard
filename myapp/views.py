from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm, UsersForm
from .models import users,Company,ProductCompany,Category,SubCategory,Product,Distributor,Customer,Purchase


""" 
     --------------------------
     E-commerce Admin Dashboard
     --------------------------
"""

def dashboard(request):
    return render(request,"admin/index.html")

def products(request):
    data = Product.objects.all()
    return render(request,"admin/products.html",{'data':data})

def insert_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        categoryID = request.POST.get('categoryID')
        PCID = request.POST.get('PCID')
        price = request.POST.get('price')
        stock = 0
        if request.POST.get('stock') == "on":
            stock = 1
        details = request.POST.get('details')
        # form = Product(PName=name,CatID_id=categoryID,PCoID_id=PCID,details=details)
        form = Product(PName=name,image=image,CatID_id=categoryID,PCoID_id=PCID,price=price,stock=stock,details=details)
        form.save()
        return redirect('products')
    else:
        category = Category.objects.all()
        productCompany = ProductCompany.objects.all()
        data = {
            'category':category,
            'productCompany':productCompany
        }
    return render(request,"admin/insert_product.html",data)

def update_product(request,id):
    product = Product.objects.get(PID=id)
    category = Category.objects.all()
    productCompany = ProductCompany.objects.all()
    data = {
            'product':product,
            'category':category,
            'productCompany':productCompany
        }
    if request.method == 'POST':
        product.PName = request.POST.get('name')
        product.CatID_id = request.POST.get('categoryID')
        product.PCoID_id = request.POST.get('PCID')
        product.details = request.POST.get('details')
        product.save()
        return redirect('products')
    return render(request,"admin/update_product.html",data)

def delete_product(request,id):
    product = Product.objects.get(PID=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request,"admin/products.html")

def categories(request):
    data = Category.objects.all()
    return render(request,"admin/categories.html",{'data':data})

def insert_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        companyID = request.POST.get('companyID')
        form = Category(CatName=name,PCID_id=companyID)
        form.save()
        return redirect('categories')
    else:
        company = Company.objects.all()
        return render(request,"admin/insert_category.html",{'company':company})

def update_category(request,id):
    category = Category.objects.get(CatID=id)
    company = Company.objects.all()
    data = {
        'category':category,
        'company':company
    }
    if request.method == 'POST':
        category.CatName = request.POST.get('name')
        category.PCID_id = request.POST.get('companyID')
        category.save()
        return redirect('categories')
    return render(request,"admin/update_category.html",data)

def delete_category(request,id):
    category = Category.objects.get(CatID=id)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request,"admin/categories.html")

def sub_categories(request):
    data = SubCategory.objects.all()
    return render(request,"admin/sub-categories.html",{'data':data})

def insert_sub_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        CatID = request.POST.get('CatID')
        form = SubCategory(name=name,CatID_id=CatID)
        form.save()
        return redirect('sub-categories')
    else:
        category = Category.objects.all()
        return render(request,"admin/insert_sub_category.html",{'category':category})

def update_sub_category(request,id):
    category = Category.objects.get(CatID=id)
    company = Company.objects.all()
    data = {
        'category':category,
        'company':company
    }
    if request.method == 'POST':
        category.CatName = request.POST.get('name')
        category.PCID_id = request.POST.get('companyID')
        category.save()
        return redirect('categories')
    return render(request,"admin/update_category.html",data)

def delete_sub_category(request,id):
    category = Category.objects.get(CatID=id)
    if request.method == 'POST':
        category.delete()
        return redirect('categories')
    return render(request,"admin/categories.html")

def distributors(request):
    data = Distributor.objects.all()
    return render(request,"admin/distributors.html",{'data':data})

def insert_distributor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        companyID = request.POST.get('companyID')
        form = Distributor(DName=name,contactNo=contact,email=email,companyID_id=companyID)
        form.save()
        return redirect('distributors')
    else:
        company = Company.objects.all()
        return render(request,"admin/insert_distributor.html",{'company':company})
    
def update_distributor(request,id):
    distributor = Distributor.objects.get(DID=id)
    company = Company.objects.all()
    data = {
        'distributor':distributor,
        'company':company
    }
    if request.method == 'POST':
        distributor.DName = request.POST.get('name')
        distributor.contactNo = request.POST.get('contact')
        distributor.email = request.POST.get('email')
        distributor.companyID_id = request.POST.get('companyID')
        distributor.save()
        return redirect('distributors')
    return render(request,"admin/update_distributor.html",data)

def delete_distributor(request,id):
    distributor = Distributor.objects.get(DID=id)
    if request.method == 'POST':
        distributor.delete()
        return redirect('distributors')
    return render(request,"admin/distributors.html")

def companies(request):
    data = Company.objects.all()
    return render(request,"admin/companies.html",{'data':data})
    
def insert_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        form = Company(companyName=name,address=address,contactNo=contact)
        form.save()
        return redirect('companies')
    else:
        return render(request,"admin/insert_company.html")

def update_company(request,id):
    company = Company.objects.get(companyID=id)
    if request.method == 'POST':
        company.companyName = request.POST.get('name')
        company.address = request.POST.get('address')
        company.contactNo = request.POST.get('contact')
        company.save()
        return redirect('companies')
    else:
        return render(request,"admin/update_company.html",{'company':company})

def delete_company(request,id):
    company = Company.objects.get(companyID=id)
    if request.method == 'POST':
        company.delete()
        return redirect('companies')
    return render(request,"admin/companies.html")

def product_companies(request):
    data = ProductCompany.objects.all()
    return render(request,"admin/product_companies.html",{'data':data})

def insert_product_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        form = ProductCompany(PCName=name,address=address,contactNo=contact,email=email)
        form.save()
        return redirect('product_companies')
    else:
        return render(request,"admin/insert_product_company.html")

def update_product_company(request,id):
    productCompany = ProductCompany.objects.get(PCID=id)
    if request.method == 'POST':
        productCompany.PCName = request.POST.get('name')
        productCompany.address = request.POST.get('address')
        productCompany.contactNo = request.POST.get('contact')
        productCompany.email = request.POST.get('email')
        productCompany.save()
        return redirect('product_companies')
    else:
        return render(request,"admin/update_product_company.html",{'productCompany':productCompany})

def delete_product_company(request,id):
    productCompany = ProductCompany.objects.get(PCID=id)
    if request.method == 'POST':
        productCompany.delete()
        return redirect('product_companies')
    return render(request,"admin/product-companies.html")

def customers(request):
    data = Customer.objects.all()
    return render(request,"admin/customers.html",{'data':data})

def insert_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        form = Customer(name=name,email=email,address=address,phone=phone)
        form.save()
        return redirect('customers')
    return render(request,"admin/insert_customer.html")

def update_customer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.address = request.POST.get('address')
        customer.phone = request.POST.get('phone')
        customer.save()
        return redirect('customers')
    return render(request,"admin/update_customer.html",{'customer':customer})

def delete_customer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    return render(request,"admin/customers.html")

def purchase(request):
    data = Purchase.objects.all()
    return render(request,"admin/purchase.html",{'data':data})

def insert_purchase(request):
    from datetime import date
    company = ProductCompany.objects.all()
    distributor = Distributor.objects.all()
    data = {
        'company':company,
        'distributor':distributor
    }
    if request.method == 'POST':
        PCoID = request.POST.get('PCoID')
        DID = request.POST.get('DID')
        qty = request.POST.get('qty')
        totalBill = request.POST.get('totalBill')
        date = date.today()
        form = Purchase(PCoID_id=PCoID,DID_id=DID,qty=qty,totalBill=totalBill,date=date)
        form.save()
        return redirect('purchase')
    return render(request,"admin/insert_purchase.html",data)

def update_purchase(request,id):
    from datetime import date
    purchase = Purchase.objects.get(id=id)
    company = ProductCompany.objects.all()
    distributor = Distributor.objects.all()
    data = {
        'purchase':purchase,
        'company':company,
        'distributor':distributor,
    }
    if request.method == 'POST':
        purchase.PCoID_id = request.POST.get('PCoID')
        purchase.DID_id = request.POST.get('DID')
        purchase.qty = request.POST.get('qty')
        purchase.totalBill = request.POST.get('totalBill')
        purchase.date = date.today()
        purchase.save()
        return redirect('purchase')
    return render(request,"admin/update_purchase.html",data)

def delete_purchase(request,id):
    purchase = Purchase.objects.get(id=id)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase')
    return render(request,"admin/purchase.html")


""" Student (Testing) """
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'success.html')
    else:
        form = StudentForm()
    return render(request, 'student_form.html',{'form':form})

def insert_data(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = UsersForm()
        return render(request,'insert_data.html',{'form':form})

def update_view(request, pk):
    instance = users.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to success URL after update
    else:
        form = UsersForm(instance=instance)
    return render(request, 'update_view.html', {'form': form})

def delete_view(request, pk):
    instance = users.objects.get(pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('success_page')  # Redirect to success URL after deletion
    return render(request, 'confirm_delete.html', {'instance' :instance})

def success_page(request):
    return render(request,'success_page.html')