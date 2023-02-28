from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Teams

# Create your views here.


# def display1(request):
#     return HttpResponse("welcome to django world")
#
#
# def display(request):
#     name="page"
#     return render(request,"welcome.html",{'obj':name})
#
# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return HttpResponse("am contact page")

def form(request):
    obj=Place.objects.all()
    obj1=Teams.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj1})

# def addition(request):
#     n1=int(request.GET['num1'])
#     n2=int(request.GET['num2'])
#     res=n1+n2
#     return render(request,'result.html',{'result':res})