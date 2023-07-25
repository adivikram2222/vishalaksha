from django.shortcuts import redirect, render
from .models import Category,Property

# Create your views here.
def index(request):
    category = Category.objects.all()
    property = Property.objects.all()
    contaxt = {
        'prop':property,
         'cat':category
       
    }
    

    return render (request,'realstate/index.html',contaxt)
def about(request):
    return render (request,'realstate/about.html')
def contact(request):
    return render (request,'realstate/contact.html')
def services(request):
    return render (request,'realstate/services.html')
def properties(request):
    category = Category.objects.all()
    property = Property.objects.all()
    contaxt = {
        'prop':property,
         'cat':category
       
    }
    return render (request,'realstate/properties.html',contaxt)
def property(request,slug):
    category = Category.objects.all()
    property = Property.objects.all()
    property = Property.objects.filter()
    if property.exists():
        property = property.first()
    else:
        return redirect('404')
    contaxt = {
        'pro':property,
        'prop':property,
        'cat':category
         
       
    }
    return render (request,'realstate/property-single.html',contaxt)