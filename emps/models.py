from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first=models.CharField(max_length=100)
    last=models.CharField(max_length=100)
    mobile=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=20,choices=[('---','---'),('Female','Female'),('Male','Male'),('Others','Others')],default='---')
    department=models.ForeignKey(Department,on_delete=models.CASCADE ,related_name='employees')
    language=models.CharField(max_length=100)
    salary=models.IntegerField()
    enrollment=models.DateTimeField(auto_now=True)
    account=models.IntegerField()
    bank=models.CharField(max_length=200)
    image=models.ImageField(default='default.jpg',upload_to='media')

    def __str__(self):
        return f"{self.first} {self.last}"
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    first_in = models.TimeField(null=True, blank=True)
    last_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Leave', 'Leave'), ('Unavailable', 'Unavailable')])

    def __str__(self):
        return f"{self.employee.first} {self.employee.last} - {self.date}"


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Approved', 'Approved'), ('Unapproved', 'Unapproved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"{self.employee.first} {self.employee.last} - {self.start_date} to {self.end_date}"
    
class Recruitment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    degree = models.CharField( max_length=10, choices = [('BCA','BCA'),('BTECH','BTECH'),('MCA','MCA'),('MBA','MBA')])

    def __str__(self):
        return f"{self.first_name} - {self.last_name} "    