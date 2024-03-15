from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('place/', views.place, name='place'),
    path('service/', views.service, name='service'),
    path('hotel/', views.hotel, name='hotel'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]