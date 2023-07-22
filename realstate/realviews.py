from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'realstate/index.html')
def about(request):
    return render (request,'realstate/about.html')
def contact(request):
    return render (request,'realstate/contact.html')
def services(request):
    return render (request,'realstate/services.html')
def properties(request):
    return render (request,'realstate/properties.html')