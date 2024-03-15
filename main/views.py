from django.shortcuts import render

from . import models

def index(request):
    """-----------Home page------------"""
    banner = models.Banner.objects.last()
    about = models.AboutUs.objects.last()
    services = models.Service.objects.all()
    places = models.Place.objects.all()
    hotels = models.Hotel.objects.all()
    blogs = models.Blog.objects.all()
    contacts = models.Contact.objects.all()
    context = {
        'banner':banner,
        'about':about,
        'places':places,
        'hotels':hotels,
        'blogs':blogs,
        'services':services,
        'contacts':contacts
    }
    return render(request, 'index.html', context)

def contact(request):
    """-----------contact-----------"""
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')


def service(request):
    """-----------service-----------"""
    services = models.Service.objects.all()

    context = {
        'services':services,    }
    return render(request, 'service.html', context)


def about(request):
    """-----------about-----------"""
    contacts = models.Contact.objects.all()
    places = models.Place.objects.all()
    hotels = models.Hotel.objects.all()
    about = models.AboutUs.objects.last()

    data = {
        'about':about,
        'places':places,
        'hotels':hotels,
        'contacts':contacts
    }
    return render(request, 'about.html', context=data)

def place(request):
    """-----------place-----------"""
    places = models.Place.objects.all()
    context = {
        'places':places,
    }
    return render(request, 'places.html', context)



def hotel(request):
    """-----------hotel-----------"""
    hotels = models.Hotel.objects.all()
    context = {
        'hotels':hotels,
    }
    return render(request, 'hotel.html', context)



def blog(request):
    """-----------blog-----------"""
    blogs = models.Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request, 'blog.html', context)