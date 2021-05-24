from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
def Home(request):
    context = {
        'variable':"HomePage"
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def servicesHome(request):
    return render(request, 'homeDelivery.html')
def MedEquip(request):
    return render(request, 'medEquip.html')
def donate(request):
    context = {
        'variable':"Donate us"
    }
    return render(request,'donate.html',context)
    
    