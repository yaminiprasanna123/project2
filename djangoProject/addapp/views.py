from django.shortcuts import render
from django.http import HttpResponse
def home(request):
# Create your views here.
    return render(request,'home.html')

def add(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("The sum is:"+str(z))
    return res