from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body> <bgcolor=yellow><center>welcome to prasannait</center></h1></body></html>""")
    return res

# Create your views here.
