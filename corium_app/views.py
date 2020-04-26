from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	
	# apps -> "name" : [ "page/slug link"
	#					 "current version",
	#					 "count total of permissions",
	#					 "count of harmful permissions",
	#					 "Rating"]

	apps = {
		"Arogya Setu": ["#", "4.4.2", "4", "3", "1"],
		"Mahakavach": ["#", "1.6.5", "16", "8", "2"]
	}
	context = {"apps": apps}
	return render(request, 'corium_app/index.html', context)