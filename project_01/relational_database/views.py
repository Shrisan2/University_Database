from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import Department
from .forms import *



# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def about(request):
    return render(request,'about.html')

def department_employees(request):
    return render(request,'department_employees.html')

def employees_projects(request):
    return render(request,'employees_projects.html')

def department_sales(request):
    return render(request,'department_sales.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def department_name_emp(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DName AS Department_Name, COUNT(Department_no) AS Total_Employees FROM department d ,employee e WHERE d.Location_no=e.Department_no GROUP BY d.location_no ORDER BY COUNT(Department_no) DESC")
        row=dictfetchall(cursor)

    return render(request,'department_name_emp.html',{'data':row})

def supervisor_supervision(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT  e.fName AS firstName,e.Minit AS middlename,e.Lname As lastname,COUNT(s.Works_for) AS Nofemp FROM EMPLOYEE AS e  LEFT OUTER JOIN EMPLOYEE AS s ON e.Ssn=s.Works_for WHERE e.Works_for IS NULL GROUP BY e.fName ORDER BY Nofemp DESC")
        row=dictfetchall(cursor)
    return render(request,'supervisor_supervision.html',{'data':row})

def extract_department_employee(request):
    if request.method=="POST":
        dname1= str(request.POST['dname'])
        statement=("SELECT Fname, Minit, Lname, Salary FROM EMPLOYEE e JOIN DEPARTMENT d ON e.Department_no=d.Location_no AND d.DName='"+dname1+"'")
        #print(dname1)
        with connection.cursor() as cursor:
             cursor.execute(statement)
             row=dictfetchall(cursor)
             return render(request,'extract_department_employee.html',{'data':row})
          #  return render(request,'extract_department_employee.html',)

def extract_emp_data(request):
    if request.method=="POST":
        fname1=str(request.POST['fname'])
        lname1=str(request.POST['lname'])
        statement=("SELECT Fname, Minit,Lname,PName,hours FROM EMPLOYEE e,WORKS_ON w,PROJECT p WHERE e.Fname='"+fname1+"' AND e.Lname='"+lname1+"' AND e.SSN=w.employee_no AND p.PNumber=w.project_no" )
        with connection.cursor() as cursor:
            cursor.execute(statement)
            row=dictfetchall(cursor)
            return render(request,'extract_emp_data.html',{'data':row})

def extract_dept_salaries(request):
    if request.method=="POST":
        dName2=str(request.POST['dname'])
      #  print (dName2)
        statement=("SELECT dName,SUM(Salary) AS Salary FROM DEPARTMENT d, EMPLOYEE e WHERE d.Dname='"+dName2+"' AND d.Location_no=e.Department_no")
        with connection.cursor() as cursor:
            cursor.execute(statement)
            row=dictfetchall(cursor)
            return render(request,'view_dept_salaries.html',{'data':row})
