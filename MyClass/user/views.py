from django.shortcuts import render
from django.http import HttpResponse

from .models import Class_User, Image_User
# class baseview
from django.views import View

# Create your views here.
def list_class(request):
	context = {'list_all': Class_User.objects.all()}
	# return HttpResponse("Heelp")
	return render(request, 'user/list_class.html', context)
# display image own member
def image_class(request, list_id):
	context = {'list_member': Class_User.objects.get(id=list_id),
				'list_all': Class_User.objects.all()}
	return render(request, 'user/image_member.html', context)


