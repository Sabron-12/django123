from django.shortcuts import render,redirect
from  django.http import HttpResponse
from  django.http import  HttpResponseRedirect
from .forms import UserForm
from .models import Person
import sqlite3 as sq
# Create your views here.
def index(request):
    people=Person.objects.all()._fetch_all()
    return render(request,"main/test.html",{"people":people})
def create(request):
    if request.method=="POST":
        klient=Person()
        klient.name=request.POST.get("name")
        klient.age=request.POST.get("age")
        klient.surname=request.POST.get("surname")
        klient.login=request.POST.get("login")
        klient.password=request.POST.get("password")
        klient.save()
        return redirect("/") #переписать
    elif request.method=="GET":
        return render(request, 'main/test.html')


'''
    if request.method=="POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        login = request.POST.get("login")
        password=request.POST.get("password")
        output="<h2>Данные о пользователе</h2><h3>Имя: {0}, Фамилия :{1}</h3><h4>Возраст :{2}</h4><h5> Пароль: {3}</h5>".format(name,surname,age,password)
            else:
        userform=UserForm()
        return render(request,'main/test.html',{"form":userform})
        '''
