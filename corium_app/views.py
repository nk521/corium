from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	context = {}
	return render(request, 'corium_app/index.html', context)