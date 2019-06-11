from django.conf.urls import url, include
from django.http import HttpResponse, request
from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import newUserForm

def index(request):
    return render(request,'appTwo/index.html')

def users(request):
    form = newUserForm()

    if request.method == 'POST':
        form = newUserForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)

    else:
        print("Erorr from invalid")

    return render(request,'appTwo/users.html', {'form':form})