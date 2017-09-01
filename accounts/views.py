from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show_profile(request):
	u = request.user
	context = {
		'u' : u,
		}
	return render(request, "accounts/profile.html", context)