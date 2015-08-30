from django.shortcuts import render
from django.http import HttpResponse
	
def home(request):
	context_dict = {}
	return render(request, 'rssSearcher/home.html', context_dict)