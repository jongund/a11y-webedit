from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PageForm
from django.http import HttpResponse
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required

# Create your views here.

def new(request):
	if request.method == 'POST':
		form_data = request.POST.copy() #get a mutable copy of the request data
		form_data['user']=(request.user).id #the form's owner becomes the
		#currently logged in user
		form=PageForm(form_data) #populate form instance with data
		if form.is_valid():
			form.save()
			pageKey = form.cleaned_data.get("web_key")
			return redirect("/pages/"+pageKey)
	else:
		form=PageForm()
		
	context = {
	'form' : form,
	}
	
	return render(request, 'pages/index.html', context)
	
#database should update as user types
#using AJAX calls
#on change event sends new data to server

#if user tries to close, ask if they want to save

#pipe safe sends raw text to db

#RUN saves before it runs

def show(request,slug):
	p=get_object_or_404(Page, web_key=slug)
	form=PageForm(request.POST or None, instance=p) 
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect("/pages/"+slug)
	context = {
		'p' : p,
		'form' : form,
	}
	return render(request, 'pages/index.html', context)

def show_all(request):
	return HttpResponse("All pages:")
	
def run(request):
	return HttpResponse("Output:")
	