from django.shortcuts import redirect, render
from .models import Category,Property
from django.core.mail import send_mail

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
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data={
            
            'name': name,
            'mail': mail,
            'mobile':mobile,
            'subject':subject,
            'message':message,

              }
        massage='''
        New massage:{}

        from:{}
        '''.format(data['message'],data['mail'])
        send_mail(data['subject'],massage,'',['payalkasayp2950@gmail.com'])


    return render (request,'realstate/contact.html',{})
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
    property_details = Property.objects.get(slug=slug)
    properte = Property.objects.filter()
    if property.exists():
        property = property.first()
    else:
        return redirect('404')
    contaxt = {
        'pro':properte,
        'prop':property,
        'cat':category,
        'propslug': property_details,  
    }
    return render (request,'realstate/property-single.html',contaxt)
def search(request):
    return render (request,'realstate/search.html')
def blog(request):
    return render (request,'realstate/blog.html')