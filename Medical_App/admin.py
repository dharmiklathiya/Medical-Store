from django.contrib import admin
from Medical_App.models import Company,Medicine,MedicalDetails,CompanyAccount,CompanyBank,Customer,CustomerRequest,Employee,EmployeeBank,EmployeeSalary,Bill,BillDetails
# Register your models here.

admin.site.register(Company),
admin.site.register(Medicine),
admin.site.register(MedicalDetails),
admin.site.register(Customer),
admin.site.register(Bill),
admin.site.register(EmployeeSalary),
admin.site.register(BillDetails),
admin.site.register(CustomerRequest),
admin.site.register(CompanyAccount),
admin.site.register(CompanyBank),
admin.site.register(EmployeeBank),