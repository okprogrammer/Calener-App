from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    return render(request,'myapp/index.html',{"entries":entries})