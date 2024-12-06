from django.shortcuts import render

# Create your views here. 

def shirt(request):
    return render(request,'shirt.html')
