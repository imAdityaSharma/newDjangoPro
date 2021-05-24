from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import ContactUs
from django.contrib import messages
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        date = datetime.today()
        Contact = ContactUs(name=name,email=email,phone=phone,query=query,date=date)
        Contact.save()
        messages.success(request, 'Thank you for reaching us, we will contact you soon.')
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
    
    