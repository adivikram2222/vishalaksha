from django.shortcuts import redirect, render
from .models import Category,Property,Blog
from django.core.mail import send_mail

# Create your views here.
def index(request):
    category = Category.objects.all()
    property = Property.objects.all()
    #property = Property.objects.filter(status='Publish')
    cat_id = request.GET.get('categories')
    # if cat_id:
    #     property = property.objects.filter(catrgory=cat_id)
    # else:
    #     property = Property.objects.filter(status='Publish')

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

def blog(request):
    category = Category.objects.all()
    property = Blog.objects.all()
    contaxt = {
        'blog':property,
         'cat':category
       
    }
    
    return render (request,'realstate/blog.html',contaxt)
def blogdetails(request,slug):
    category = Category.objects.all()
    property = Blog.objects.all()
    property_details = Blog.objects.get(slug=slug)
    properte = Blog.objects.filter()
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
    return render (request,'realstate/blogdetails.html',contaxt)
# def search(request):
#     query = request.GET.get('query')
#     property = Property.objects.filter(name__icontains=query)

#     contaxt={ 
#         'prop': property,


#     }
    

#     return render (request,'realstate/search.html', contaxt)



def search(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('query')
        if query_name:
            results = Property.objects.filter(name_of_property=query_name)
            results2 = Property.objects.filter(city=query_name)
            results3 = Property.objects.filter(furnished_status=query_name)
            results4 = Property.objects.filter(transaction_type=query_name)
            contaxt={
                "results":results,
                "results2":results2,
                "results3":results3,
                "results4":results4,

                }
            return render(request, 'realstate/search.html',contaxt)

    return render(request, 'realstate/search.html')
