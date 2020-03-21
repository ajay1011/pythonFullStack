from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_2(request):
    return HttpResponse("<em> My second App</em>")

def help(request):
    return render(request,'app_two/help.html',context=None)
