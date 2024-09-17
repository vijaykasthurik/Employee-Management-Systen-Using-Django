from django.shortcuts import render
from django.http import HttpResponse
from .models import Employeedetails
# Create your views here.
def index(request):
    lists=Employeedetails.objects.all()
    return render(request,'index.html',{'lists':lists})

