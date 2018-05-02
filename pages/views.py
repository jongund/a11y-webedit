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
from accounts.models import Profile

def show_samples(request):
	tags    = Tag.objects.all()
	samples = Page.objects.filter(sample=True).order_by('title')
	context = {
	  'title': 'Samples',
 		'tags':tags,
		'samples':samples
	}
	return render(request, 'pages/samples.html', context)

#THIS FUNCTION IS LIKELY UNNECESSARY AND CAN BE MERGED WITH SHOW
def new(request):
	if request.user.is_anonymous():
		user = None
	else:
		user = request.user
		try:
			profile = Profile.objects.get(user=user)
		except:
			profile = Profile(user=user)
			profile.save()

	if request.method == 'POST':

		form = PageForm(request.POST) #populate form instance with data
		form.user = user

		if form.is_valid():
			page = form.save()
			page.user = user
			page.save()

			if page.user:
				return redirect(reverse('show',args=[page.user.profile.slug, page.slug]))
			else:
				return redirect(reverse('show_anon',args=[page.slug]))

	else:
		page = Page(user=user, slug=get_random_string(length=6).lower())
		form = PageForm(instance=page)

	context = {
	'title' : 'New Page',
	'form' : form,
	'sameUser' : True,
	}

	return render(request, 'pages/index.html', context)

#def new_anon

def show_anon(request, page_slug):
	page = get_object_or_404(Page, user=None, slug=page_slug)

	form=PageForm(request.POST or None, instance=page)

	if request.method == 'POST':

		form=PageForm(request.POST,instance=page)

		if form.is_valid():
			form.save()

			return redirect(reverse('show_anon',args=[page.slug]))
	context = {
		'title' : 'Edit Page',
		'p' : page,
		'form' : form
	}
	return render(request, 'pages/index.html', context)

def run_anon(request, page_slug):
	page = get_object_or_404(Page,slug=page_slug)

	html = '<!DOCTYPE html>\n'
	html += '<html>\n'
	html += '  <head>\n'

	if page.htmlHead.find('<title>') < 0:
		html += '    <title>\n'
		html += '      ' + page.title + '\n'
		html += '    </title>\n'

	html += '    <script src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>\n'
	html += page.htmlHead

	if len(page.css):
		html += '    <style type="text/css">\n'
		html += page.css
		html += '    </style>\n'

	if len(page.javascript):
		html += '    <script type="text/javascript">\n'
		html += page.javascript
		html += '    </script>\n'

	html += '  </head>\n'
	html += '  <body>\n'
	html += page.htmlBody
	html += '  </body>\n'
	html += '</html>\n'

	return HttpResponse(html)

def copy_anon(request, page_slug):
	page=get_object_or_404(Page, slug=page_slug, user=None)
	copy_title = "Copy of '"+page.title+"'"
	if request.user.is_anonymous():
		user = None
	else:
		user = request.user

	copy = Page(user=user, title=copy_title, description=page.description,htmlHead=page.htmlHead,\
	htmlBody=page.htmlBody,css=page.css,javascript=page.javascript,\
	slug=get_random_string(length=8).lower())

	try:
		copy.save()
	except:
		return redirect(reverse('show_anon',args=[slug]))

	if user:
		return redirect(reverse('show',args=[copy.user.profile.slug, copy.slug]))
	else:
		return redirect(reverse('show_anon',args=[copy.slug]))


#database should update as user types
#using AJAX calls
#on change event sends new data to server

#if user tries to close, ask if they want to save

#pipe safe sends raw text to db

#RUN saves before it runs

def show(request, profile_slug, page_slug):
	username = Profile.objects.get(slug=profile_slug).user.username

	user = get_object_or_404(User, username=username)

	try:
		page = Page.objects.get(user=user, slug=page_slug)
	except:
		page = get_object_or_404(Page,webKey=page_slug,user=user)

	form = PageForm(request.POST or None, instance=page)

	user = request.user

	if request.method == 'POST':
		form_data = request.POST.copy()
		form_data['user']=(request.user).id
		form=PageForm(form_data,instance=page)
		if form.is_valid():
			form.save()

			return redirect(reverse('show', args=[user.profile.slug, page.slug]))

	context = {
	  'title' : 'Edit Page',
		'p' : page,
		'form' : form,
		'sameUser' : request.user.username == username
	}
	return render(request, 'pages/index.html', context)

def show_all(request,profile_slug):
	username = Profile.objects.get(slug=profile_slug).user.username

	all_pages = Page.objects.filter(user=get_object_or_404(User,username=username))
	user = User.objects.get(username=username)
	name = user.first_name + ' ' + user.last_name

	if not len(name) > 1:
		name = username

	context = {
		'title' : name + '\'s Pages',
		'all_pages' : all_pages,
		'name' : name,
	}
	return render(request, 'pages/all_pages.html', context)

def run(request,page_slug,profile_slug):
	username = Profile.objects.get(slug=profile_slug).user.username

	user = get_object_or_404(User, username=username)

	try:
		page = Page.objects.get(user=user, slug=page_slug)
	except:
		page = get_object_or_404(Page,webKey=page_slug,user=user)

	html = '<!DOCTYPE html>\n'
	html += '<html>\n'
	html += '  <head>\n'

	if page.htmlHead.find('<title>') < 0:
		html += '    <title>\n'
		html += '      ' + page.title + '\n'
		html += '    </title>\n'

	html += '    <script src="https://code.jquery.com/jquery-3.2.1.js" integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" crossorigin="anonymous"></script>\n'
	html += page.htmlHead

	if len(page.css):
		html += '    <style type="text/css">\n'
		html += page.css
		html += '    </style>\n'

	if len(page.javascript):
		html += '    <script type="text/javascript">\n'
		html += page.javascript
		html += '    </script>\n'


	html += '  </head>\n'
	html += '  <body>\n'
	html += page.htmlBody
	html += '  </body>\n'
	html += '</html>\n'

	return HttpResponse(html)

def delete(request, page_slug, profile_slug):
	user = Profile.objects.get(slug=profile_slug).user
	username = user.username

	context = {
		'sameUser' : False
	}
	if request.user.username != username:
		return render(request, 'pages/index.html', context)
	p=get_object_or_404(Page, slug=page_slug, user=get_object_or_404(User, username=username))
	p.delete()
	if request.user.is_anonymous():
		return redirect(reverse('new'))
	else:
		return redirect(reverse('show_all', args=[user.profile.slug]))

def copy(request, page_slug, profile_slug):
	username = Profile.objects.get(slug=profile_slug).user.username

	page = get_object_or_404(Page, slug=page_slug, user=get_object_or_404(User, username=username))

	copy_title = "Copy of '" + page.title + "'"
	if request.user.is_anonymous():
		user = None
	else:
		user = request.user

	copy = Page(user=user, title=copy_title, description=page.description,htmlHead=page.htmlHead,\
	htmlBody=page.htmlBody,css=page.css,javascript=page.javascript,\
	slug=get_random_string(length=6).lower())

	try:
		copy.save()
	except:
		return redirect(reverse('show',args=[user.profile.slug, slug]))

	if user:
		return redirect(reverse('show',args=[user.profile.slug, copy.slug]))
	else:
		return redirect(reverse('show_anon',args=[copy.slug]))


