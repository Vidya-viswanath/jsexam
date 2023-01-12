from django.shortcuts import render

# Create your views here.

def biodata_home(request) :
    return render(request,'biodata/home.html') 
