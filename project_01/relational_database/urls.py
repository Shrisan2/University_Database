from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('about',views.about,name='about'),
    path('department_employees',views.department_employees,name='department_employees'),
    path('view_employees_projects',views.employees_projects,name='view_employees_projects'),
    path('view_department_sales',views.department_sales,name='view_department_sales'),
    path('view_department_name_emp',views.department_name_emp,name='view_department_name_emp'),
    path('supervisor_supervision',views.supervisor_supervision,name='supervisor_supervision'),
    path('extract_department_employee', views.extract_department_employee,name="extract_department_employee"),
    path('extract_emp_data',views.extract_emp_data,name="extract_emp_data"),
    path('extract_dept_salaries',views.extract_dept_salaries,name="extract_dept_salaries"),
]