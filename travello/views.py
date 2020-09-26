from django.shortcuts import render
from django.http import HttpResponse ,request
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
