from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.


@login_required
def homeViews(request):
    superuser_count = User.objects.count()
    department = Department.objects.all()
    employees = Employee.objects.all()
    return render(request, 'emps/home.html', {'employees': employees, 'department':department,'superuser_count': superuser_count})

@login_required
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'emps/employee_add.html', {'form': form})


@login_required
def employee_all(request):
    employees = Employee.objects.all()
    return render(request, 'emps/employees.html', {'employees': employees})

@login_required
def employee_edit(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_view',employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'emps/employee_add.html', {'form': form})

@login_required
def employee_delete(request, id):
    employee = Employee.objects.get(id=id )
    employee.delete()
    return redirect('employee_all')

@login_required
def employee_view(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'emps/employee_view.html', {'employee': employee})

@login_required
def departmentViews(request):
    department=Department.objects.all()
    if request.method=='POST':
        form=DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=DepartmentForm()
    context={
        'form':form,
        'department':department,
    }    
    return render(request,'emps/department.html',context)        

@login_required
def department_detail(request,id):
    department = Department.objects.get(id=id)
    employees = department.employees.all()
    return render(request, 'emps/department_detail.html', {'department': department, 'employees': employees})

@login_required
def department_edit(request, id):
    department = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_detail',department.id)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'emps/department.html', {'form': form})

@login_required
def department_delete(request, id):
    department = Department.objects.get(id=id )
    department.delete()
    return redirect('home')

@login_required
def attendance_view(request):
    if request.method == 'POST':
        
        # Sign In
        if 'sign_in' in request.POST:
            employee_id = request.POST.get('employee_id')
            status = request.POST.get('status')
            employee = Employee.objects.get(id=employee_id)

            # Check if an attendance record already exists for the current date
            existing_attendance = Attendance.objects.filter(employee=employee, date=timezone.now().date()).first()
            if existing_attendance:
                return redirect('attendance')
            
            Attendance.objects.create(
                employee=employee,
                status=status,
                first_in=timezone.now().time(),
                date=timezone.now().date()
            )
        
        # Sign Out
        if 'sign_out' in request.POST:
            attendance_id = request.POST.get('attendance_id')
            attendance = Attendance.objects.get(id=attendance_id)
            if attendance:
                attendance.last_out = timezone.now().time()
                attendance.save()
        
        return redirect('attendance')
    
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    current_date = timezone.now().date() 
    return render(request, 'emps/attendance.html', {'employees': employees, 'attendances': attendances, 'current_date': current_date})

@login_required
def leave_view(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')
        employee = Employee.objects.get(id=employee_id)
        
        Leave.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            status=status
        )
        
        return redirect('leave')
    
    employees = Employee.objects.all()
    leaves = Leave.objects.all()
    return render(request, 'emps/leave.html', {'employees': employees, 'leaves': leaves,})

def hompepage(request):
    return render(request,'emps/homepage.html')

def recruitmentform(request):
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RecruitmentForm()
    return render(request, 'emps/recruitmentform.html', {'form': form})

@login_required
def recruitment_view(request):
    recruitment = Recruitment.objects.all()
    return render(request, 'emps/recruitment.html', {'recruitment': recruitment})

@login_required
def recruitment_delete(request, id):
    recruitment = Recruitment.objects.get(id=id )
    recruitment.delete()
    return redirect('recruitment')

@login_required
def payroll(request):
    employees = Employee.objects.all()
    paid_employees = []

    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        paid_employees.append(employee_id)

    employees = employees.exclude(id__in=paid_employees)
    return render(request, 'emps/payroll.html', {'employees': employees, 'paid_employees': paid_employees})

def signupView(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()    
    return render(request,'emps/signup.html',{'form':form})