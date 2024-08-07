from django.urls import path
from .views import *
from django.contrib.auth import views as auth

urlpatterns = [
     path('home/', homeViews, name='home'),
     path('employees/add/', employee_add, name='employee_add'),
     path('employees/', employee_all, name='employee_all'),
     path('employee/edit/<int:id>/',employee_edit,name='employee_edit'),
     path('employee/delete/<int:id>/',employee_delete,name='employee_delete'),
     path('employee/view/<int:id>/',employee_view,name='employee_view'),
     path('department/',departmentViews,name='department'),
     path('department/detail/<int:id>/',department_detail,name='department_detail'),
     path('department/edit/<int:id>/',department_edit,name='department_edit'),
     path('department/delete/<int:id>/',department_delete,name='department_delete'),
     path('attendance/', attendance_view, name='attendance'),
     path('leave/', leave_view, name='leave'),
     path('',hompepage,name = 'homepage'),
     path('recruitmentform/',recruitmentform,name='recruitmentform'),
     path('recruit/',recruitment_view,name='recruitment'),
     path('recruitment/delete/<int:id>',recruitment_delete,name='recruitment_delete'),
     path('payroll',payroll,name='payroll'),
     path('login/',auth.LoginView.as_view(template_name='emps/login.html'),name='login'),
     path('signup/',signupView,name='signup'),

]   
