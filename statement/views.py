from django.shortcuts import render
from .models import *
from .forms import NameForm

# Create your views here.
def index(request):
	return render(request,'index.html',{})

def display_account(request):
	data=request.GET['fulltext']
	item=xyz.objects.all()
	context={

	'items':item,
	'fulltext':data,
	}
	return render(request,'index.html',context)

def displayall(request):
	dataAll=xyz.objects.all()
	context={
	'dataAll':dataAll
	}
	return render(request,'displayall.html',context)