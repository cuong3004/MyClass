from django.shortcuts import render
from django.http import HttpResponse

# app user

# Create your views here.
def Index(request):
	return HttpResponse("xin chao")


