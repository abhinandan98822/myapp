from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . forms import RegisterForm
from . models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate


# Create your views here.
@csrf_exempt
def RegsiterView(request):
    if request.method=='POST':
        form1= RegisterForm(request.POST)
        if form1.is_valid():
            form1.save() 
            return HttpResponse('data is saved')
    else:
        form1= RegisterForm()
        context={'form':form1}
    return render(request,'register.html',context)


