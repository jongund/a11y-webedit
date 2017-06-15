from django.shortcuts import render, redirect, get_object_or_404
from .models import Page
from .forms import PageForm
from django.http import HttpResponse
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required

#THIS FUNCTION IS LIKELY UNNECESSARY AND CAN BE MERGED WITH SHOW
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
	"""try:
		p = Page.objects.get(web_key=slug)
	except: 
		form=PageForm()"""
	form=PageForm(request.POST or None, instance=p) 
	if request.method == 'POST':
		form_data = request.POST.copy()
		form_data['user']=(request.user).id
		form=PageForm(form_data,instance=p)
		if form.is_valid():
			form.save()
			pageKey = form.cleaned_data.get("web_key")
			return redirect("/pages/"+pageKey)
	context = {
		'p' : p,
		'form' : form,
	}
	return render(request, 'pages/index.html', context)

def show_all(request):
	all_pages = [(i.title,i.description,i.lastUpdated,i.web_key) for i in Page.objects.filter(\
	user=request.user)]
	context = {
		'all_pages' : all_pages,
	}
	return render(request, 'pages/all_pages.html', context)
	#return HttpResponse("<h2>All pages:</h2>"+all_pages+"</ul>")
	
def run(request,slug):
	p=get_object_or_404(Page,web_key=slug)
	web_page="<head>"+p.htmlHead+"</head>"+"<style>"+p.css+"</style>"+\
	p.htmlBody+"<script src='https://code.jquery.com/jquery-3.2.1.js'\
	integrity='sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE='crossorigin='anonymous'></script>\
	<script>"+p.javascript+"</script>"
	return HttpResponse(web_page)
	
def delete(request, slug):
	p=get_object_or_404(Page, web_key=slug)
	p.delete()
	return redirect("/pages/all")