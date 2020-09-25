from django.shortcuts import render
from django.http import HttpResponse ,request
from .models import Destination
# Create your views here.
def index(request):
    dest_1 = Destination()
    dest_1.image = 'destination_1.jpg'
    dest_1.title = 'Paris'
    dest_1.description = 'The city never sleep'
    dest_1.price = 850
    dest_1.offer = False

    dest_2 = Destination()
    dest_2.image = 'destination_2.jpg'
    dest_2.title = 'London'
    dest_2.description = 'The city never sleep'
    dest_2.price = 850
    dest_2.offer = True

    dest_3 = Destination()
    dest_3.image = 'destination_3.jpg'
    dest_3.title = 'Rome'
    dest_3.description = 'The city never sleep'
    dest_3.price = 850
    dest_3.offer = False

    dests = [dest_1,dest_2,dest_3]
    return render(request,'index.html',{'dests':dests})
