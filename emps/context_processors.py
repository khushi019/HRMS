from .models import Department

def department_names(request):
    departments = Department.objects.all()
    return {'departments': departments}
