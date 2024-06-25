from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Urls
    path("admin/",views.dashboard,name="dashboard"),
    path("admin/products",views.products,name="products"),
    path("admin/products/insert",views.insert_product,name="products.insert"),
    path("admin/products/update/<int:id>",views.update_product,name="products.update"),
    path("admin/products/delete/<int:id>",views.delete_product,name="products.delete"),
    path("admin/categories",views.categories,name="categories"),
    path("admin/categories/insert",views.insert_category,name="categories.insert"),
    path("admin/categories/update/<int:id>",views.update_category,name="categories.update"),
    path("admin/categories/delete/<int:id>",views.delete_category,name="categories.delete"),
    path("admin/sub-categories",views.sub_categories,name="sub-categories"),
    path("admin/sub-categories/insert",views.insert_sub_category,name="sub-categories.insert"),
    path("admin/sub-categories/update/<int:id>",views.update_sub_category,name="sub-categories.update"),
    path("admin/sub-categories/delete/<int:id>",views.delete_sub_category,name="sub-categories.delete"),
    path("admin/distributors",views.distributors,name="distributors"),
    path("admin/distributors/insert",views.insert_distributor,name="distributors.insert"),
    path("admin/distributors/update/<int:id>",views.update_distributor,name="distributors.update"),
    path("admin/distributors/delete/<int:id>",views.delete_distributor,name="distributors.delete"),
    path("admin/companies",views.companies,name="companies"),
    path("admin/companies/insert",views.insert_company,name="companies.insert"),
    path("admin/companies/update/<int:id>",views.update_company,name="companies.update"),
    path("admin/companies/delete/<int:id>",views.delete_company,name="companies.delete"),
    path("admin/product-companies",views.product_companies,name="product_companies"),
    path("admin/product-companies/insert",views.insert_product_company,name="product_companies.insert"),
    path("admin/product-companies/update/<int:id>",views.update_product_company,name="product_companies.update"),
    path("admin/product-companies/delete/<int:id>",views.delete_product_company,name="product_companies.delete"),
    path("admin/customers",views.customers,name="customers"),
    path("admin/customers/insert",views.insert_customer,name="customers.insert"),
    path("admin/customers/update/<int:id>",views.update_customer,name="customers.update"),
    path("admin/customers/delete/<int:id>",views.delete_customer,name="customers.delete"),
    path("admin/purchase",views.purchase,name="purchase"),
    path("admin/purchase/insert",views.insert_purchase,name="purchase.insert"),
    path("admin/purchase/update/<int:id>",views.update_purchase,name="purchase.update"),
    path("admin/purchase/delete/<int:id>",views.delete_purchase,name="purchase.delete"),
    
    # Forms
    path("student_form/",views.student_form,name="student_form"),
    path("insert_data/",views.insert_data,name="insert_data"),
    path("success_page/",views.success_page,name="success_page"),
    path('update/<int:pk>/', views.update_view,name='update'),
    path('delete/<int:pk>/', views.delete_view,name='delete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


