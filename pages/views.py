from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PageForm
from django.http import HttpResponse
#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from django.utils.crypto import get_random_string

from .models import Page
from .models import Tag

def show_samples(request):
	tags    = Tag.objects.all()
	samples = Page.objects.filter(sample=True)
	context = {
		'tags':tags,
		'samples':samples
	}
	return render(request, 'pages/samples.html', context)

#THIS FUNCTION IS LIKELY UNNECESSARY AND CAN BE MERGED WITH SHOW
def new(request):
	if request.method == 'POST':
		form_data=request.POST.copy() #get a mutable copy of the request data
		form_data['user']=(request.user).id #the form's owner becomes the
		#currently logged in user
		form=PageForm(form_data) #populate form instance with data
		if form.is_valid():
			form.save()
			pageKey=form.cleaned_data.get("webKey")
			if request.user.is_anonymous:
				return redirect(reverse('show_anon',args=[pageKey]))
			else:
				return redirect(reverse('show',args=[request.user.username, pageKey]))
	else:
		p = Page(webKey=get_random_string(length=6).lower())
		form=PageForm(instance=p)

	context = {
	'form' : form,
	'sameUser' : True,
	}

	return render(request, 'pages/index.html', context)

#def new_anon

def show_anon(request, slug):
	p=get_object_or_404(Page, webKey=slug)
	form=PageForm(request.POST or None, instance=p)
	if request.method == 'POST':
		form_data = request.POST.copy()
		#form_data['user']=(request.user).id
		form=PageForm(form_data,instance=p)
		if form.is_valid():
			form.save()
			pageKey = form.cleaned_data.get("webKey")
			return redirect(reverse('show_anon',args=[pageKey]))
	context = {
		'p' : p,
		'form' : form
	}
	return render(request, 'pages/index.html', context)

def run_anon(request,slug):
	p=get_object_or_404(Page,webKey=slug)
	web_page="<head>"+p.htmlHead+"</head>"+\
	"<style>"+p.css+"</style>"+\
	p.htmlBody+"<script src='https://code.jquery.com/jquery-3.2.1.js'\
	integrity='sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE='crossorigin='anonymous'></script>\
	<script>"+p.javascript+"</script>"
	return HttpResponse(web_page)


#database should update as user types
#using AJAX calls
#on change event sends new data to server

#if user tries to close, ask if they want to save

#pipe safe sends raw text to db

#RUN saves before it runs
def show(request,slug,username):
	p=get_object_or_404(Page, webKey=slug, user=get_object_or_404(User,username=username))
	form=PageForm(request.POST or None, instance=p)
	if request.method == 'POST':
		form_data = request.POST.copy()
		form_data['user']=(request.user).id
		form=PageForm(form_data,instance=p)
		if form.is_valid():
			form.save()
			pageKey = form.cleaned_data.get("webKey")
			return redirect(reverse('show',args=[request.user.username,pageKey]))
	context = {
		'p' : p,
		'form' : form,
		'sameUser' : request.user.username == username
	}
	return render(request, 'pages/index.html', context)

def show_all(request):
	all_pages = Page.objects.filter(user=request.user)
	context = {
		'all_pages' : all_pages,
	}
	return render(request, 'pages/all_pages.html', context)

def run(request,slug,username):
	p=get_object_or_404(Page,webKey=slug,user=get_object_or_404(User, username=username))
	html = '<!DOCTYPE html>\n'
	html += '<html>\n'
	html += '  <head>\n'

	html += '    <title>\n'
	html += '      ' + p.title + '\n'
	html += '    </title>\n'

	if len(p.css):
		html += '    <style type="text/css">\n'
		html += p.css
		html += '    </style>\n'

 	if len(p.javascript):
		html += '    <script type="text/javascript">\n'
		html += p.javascript
		html += '    </script>\n'

 	html += '    <script src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>\n'
	html += p.htmlHead

	html += '  </head>\n'
	html += '  <body>\n'
	html += p.htmlBody
	html += '  </body>\n'
	html += '</html>\n'

	return HttpResponse(html)

def delete(request, slug, username):
	context = {
		'sameUser' : False
	}
	if request.user.username != username:
		return render(request, 'pages/index.html', context)
	p=get_object_or_404(Page, webKey=slug, user=get_object_or_404(User, username=username))
	p.delete()
	if request.user.is_anonymous():
		return redirect(reverse('new'))
	else:
		return redirect(reverse('show_all'))

def copy(request, slug, username):
	p=get_object_or_404(Page, webKey=slug, user=get_object_or_404(User,username=username))
	copy_title = "Copy of '"+p.title+"'"
	copy_description = "'"+p.description+"'"
	copy = Page(title=copy_title,description=copy_description,htmlHead=p.htmlHead,\
	htmlBody=p.htmlBody,css=p.css,javascript=p.javascript,\
	webKey=get_random_string(length=6).lower(),user=request.user)
	try:
		copy.save()
	except:
		return redirect(reverse('show',args=[request.user.username,p.webKey]))
	return redirect(reverse('show',args=[request.user.username,copy.webKey]))
