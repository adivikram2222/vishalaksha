from pyexpat.errors import messages
from django.http import BadHeaderError
from django.shortcuts import redirect, render,HttpResponse
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def index(request):
    # faq = FAQ.objects.all()
    # category = categorie.objects.all()
    # first_course = course.objects.get(pk=1)
    # courses = course.objects.all()
    # articles = Article.objects.filter()
    # # print(first_course)
    # context = {
    #     'courses':courses,
    #     'category':category, 
    #     'first_course':first_course,
    #     'faq':faq,
    #     'article' : articles,
    # }
    # print(course)
    # print(articles)
    return render(request,'main/index.html',)


def index(request):
    return render(request,'main/index.html',)
def about(request):
    return render(request,'main/about.html',)
def contact(request):
    return render(request,'main/contact.html',)
def services(request):
    return render(request,'main/services.html',)

def contact_us(request):
    if request.method == 'GET':
        form = contact_us()
    else:
        form = contact_us(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['californiamikegreen@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
   
