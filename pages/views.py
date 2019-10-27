from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import PageForm, ProfileForm, PageFormWithCodeMirror
from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from django.utils.crypto import get_random_string

from .models import Page
from .models import Tag
from accounts.models import Profile


def show_samples(request):
    tags = Tag.objects.all()
    samples = Page.objects.filter(sample=True).order_by('title')
    context = {
        'title': 'Samples',
        'tags': tags,
        'samples': samples
    }
    return render(request, 'pages/samples.html', context)


# THIS FUNCTION IS LIKELY UNNECESSARY AND CAN BE MERGED WITH SHOW
def new(request):
    if request.user.is_anonymous:
        user = None
        profile = None
    else:
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except:
            profile = Profile(user=user)
            profile.save()

    if request.method == 'POST':

        if not request.user.is_anonymous:
            if request.user.profile.useCodeMirror:
                pageForm = PageFormWithCodeMirror(request.POST)  # populate form instance with data
            else:
                pageForm = PageForm(request.POST)
            profileForm = ProfileForm(request.POST or None, instance=profile)
        else:
            pageForm = PageForm(request.POST)
            pageForm.user = Profile.objects.get(user__username="anon")[0]['id']

        if pageForm.is_valid():
            page = pageForm.save()
            page.user = user
            page.save()

            if page.user:
                return redirect(reverse('show', args=[page.user.profile.slug, page.slug]))
            else:
                return redirect(reverse('show_anon', args=[page.slug]))

    else:
        if not request.user.is_anonymous:
            page = Page(user=user, slug=get_random_string(length=6).lower())
            if request.user.profile.useCodeMirror:
                pageForm = PageFormWithCodeMirror(instance=page)  # populate form instance with data
            else:
                pageForm = PageForm(instance=page)
            profileForm = ProfileForm(request.POST or None, instance=profile)
        # else:
        #     pageForm = PageForm(instance=page)
        #     pageForm.user = Profile.objects.get(user__username="anon")[0]['id']

        # profileForm = ProfileForm(request.POST or None, instance=profile)

    # if profile is None:
    #     profile = Profile.objects.get(user__username="anon")
    #     profileForm = ProfileForm(request.POST or None, instance=profile)

    context = {
        'title': 'New Page',
        'pageForm': pageForm,
        'profileForm': profileForm,
        'sameUser': True,
    }

    if not request.user.is_anonymous:
        if request.user.profile.useCodeMirror:
            response = render(request, 'pages/index.html', context)
        else:
            response = render(request, 'pages/index_without_codemirror.html', context)
    # if profile is None:
    #     response.set_cookie(key='isUserAnonymous', value=True)
    #     response.set_cookie(key='useCodeMirror', value=True)

    return response


# def new_anon

def show_anon(request, page_slug):
    page = get_object_or_404(Page, user=None, slug=page_slug)

    pageForm = PageForm(request.POST or None, instance=page)

    if request.method == 'POST':

        pageForm = PageForm(request.POST, instance=page)

        if pageForm.is_valid():
            pageForm.save()

            response = redirect(reverse('show_anon', args=[page.slug]))
            # response.set_cookie(key='useCodeMirror', value=not request.COOKIES.get('useCodeMirror'))

            return response

    profile = Profile.objects.get(user__username='anon')
    profileForm = ProfileForm(request.POST or None, instance=profile)

    context = {
        'title': 'Edit Page',
        'p': page,
        'profileForm': profileForm,
        'pageForm': pageForm,
        'sameUser': True
    }

    response = render(request, 'pages/index.html', context)
    profileForm = {'useCodeMirror': True}
    context['profileForm'] = profileForm
    # response.set_cookie(key='useCodeMirror', value=True)

    return response


def run_anon(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)

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
    page = get_object_or_404(Page, slug=page_slug, user=None)
    copy_title = "Copy of '" + page.title + "'"
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user

    copy = Page(user=user, title=copy_title, description=page.description, htmlHead=page.htmlHead, \
                htmlBody=page.htmlBody, css=page.css, javascript=page.javascript, \
                slug=get_random_string(length=8).lower())

    try:
        copy.save()
    except:
        return redirect(reverse('show_anon', args=[slug]))

    if user:
        return redirect(reverse('show', args=[copy.user.profile.slug, copy.slug]))
    else:
        return redirect(reverse('show_anon', args=[copy.slug]))


# database should update as user types
# using AJAX calls
# on change event sends new data to server

# if user tries to close, ask if they want to save

# pipe safe sends raw text to db

# RUN saves before it runs

def show(request, profile_slug, page_slug):
    profile = Profile.objects.get(slug=profile_slug)
    username = profile.user.username

    user = get_object_or_404(User, username=username)

    try:
        page = Page.objects.get(user=user, slug=page_slug)
    except:
        page = get_object_or_404(Page, webKey=page_slug, user=user)

    if request.user.profile.useCodeMirror:
        pageForm = PageFormWithCodeMirror(request.POST or None, instance=page)
    else:
        pageForm = PageForm(request.POST or None, instance=page)


    profileForm = ProfileForm(request.POST or None, instance=profile)

    user = request.user

    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['user'] = (request.user).id
        if request.user.profile.useCodeMirror:
            pageForm = PageFormWithCodeMirror(form_data, instance=page)
        else:
            pageForm = PageForm(form_data, instance=page)
        profileForm = ProfileForm(form_data, instance=profile)
        if pageForm.is_valid():
            pageForm.save()
            # profileForm.save()

            return redirect(reverse('show', args=[user.profile.slug, page.slug]))

    context = {
        'title': 'Edit Page',
        'p': page,
        'pageForm': pageForm,
        'profileForm': profileForm,
        'sameUser': request.user.username == username
    }

    if request.user.profile.useCodeMirror:
        return render(request, 'pages/index.html', context)
    else:
        return render(request, 'pages/index_without_codemirror.html', context)



def show_all(request, profile_slug):
    username = Profile.objects.get(slug=profile_slug).user.username

    all_pages = Page.objects.filter(user=get_object_or_404(User, username=username))
    user = User.objects.get(username=username)
    name = user.first_name + ' ' + user.last_name

    if not len(name) > 1:
        name = username

    context = {
        'title': name + '\'s Pages',
        'all_pages': all_pages,
        'name': name,
    }
    return render(request, 'pages/all_pages.html', context)


def run(request, page_slug, profile_slug):
    username = Profile.objects.get(slug=profile_slug).user.username

    user = get_object_or_404(User, username=username)

    try:
        page = Page.objects.get(user=user, slug=page_slug)
    except:
        page = get_object_or_404(Page, webKey=page_slug, user=user)

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
        'sameUser': False
    }
    if request.user.username != username:
        return render(request, 'pages/index.html', context)
    p = get_object_or_404(Page, slug=page_slug, user=get_object_or_404(User, username=username))
    p.delete()
    if request.user.is_anonymous:
        return redirect(reverse('new'))
    else:
        return redirect(reverse('show_all', args=[user.profile.slug]))


def copy(request, page_slug, profile_slug):
    username = Profile.objects.get(slug=profile_slug).user.username

    page = get_object_or_404(Page, slug=page_slug, user=get_object_or_404(User, username=username))

    copy_title = "Copy of '" + page.title + "'"
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user

    copy = Page(user=user, title=copy_title, description=page.description, htmlHead=page.htmlHead, \
                htmlBody=page.htmlBody, css=page.css, javascript=page.javascript, \
                slug=get_random_string(length=6).lower())

    try:
        copy.save()
    except:
        return redirect(reverse('show', args=[user.profile.slug, slug]))

    if user:
        return redirect(reverse('show', args=[user.profile.slug, copy.slug]))
    else:
        return redirect(reverse('show_anon', args=[copy.slug]))
