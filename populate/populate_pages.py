import django
import json
import sys
import os

fp = os.path.realpath(__file__)
path, filename = os.path.split(fp)
webedit_path = os.path.split(path)[0]

sys.path.append(webedit_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebEdit.settings")

from django.conf import settings

django.setup()

from django.core.exceptions 	import ObjectDoesNotExist
from pages.models import Page
from pages.models import Tag
from django.contrib.auth.models import User



def create_page(page):

	try:
		print("Update Page: " + page.webKey),
		p = Page.objects.get(webKey=page.webKey, user=admin_user)

		p.title       = page.title
		p.description = page.description
		p.htmlHead    = page.htmlHead
		p.htmlBody    = page.htmlBody
		p.sample      = page.sample

	except ObjectDoesNotExist:
		print("Create Page: " + page.webKey)
		p = Page(user=admin_user, webKey= page.webKey, title=page.title, description=page.description, htmlHead = page.htmlHead, htmlBody=page.htmlBody, sample=page.sample)

	p.save()
	p.tags.remove()
	p.save()

	for t in page.tags.split(' '):
		try:
			tag = Tag.objects.get(slug=t)
			p.tags.add(tag)
			p.save()
		except ObjectDoesNotExist:
			print('Tag not found: ' + tag)

# Page.objects.all().delete()

admin_user = User.objects.get(username=settings.ADMIN_USERNAME)

page = type("myobj",(object,),dict(webKey='', title='', description='', htmlHead='', htmlBody='', css='', javascript='', tags='', sample=False))
page.webKey = 'landmark1-hw'
page.title = 'Homework: Landmark 1'
page.description = 'Homework problem for A11yBadging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""
page.tags = 'landmarks'
page.sample = True


page.htmlBody = """
    <div class="container">
      <div class="header clearfix">
        <div>
          <ul class="nav nav-pills float-right">
            <li class="nav-item">
              <a class="nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="jumbotron">
        <h1 class="display-3">ARIA Landmarks, Headings and Page Titles</h1>
        <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
      </div>

      <div class="row">
        <div class="col-sm-12">
           <h1>
           Add Landmarks Using Roles
           </h1>
        </div>
      </div>

      <div class="row marketing">
        <div class="col-sm-6">
          <h4>Topic A</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Topic B</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Topic C</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>

        <div class="col-sm-6">
          <h4>Topic D</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Topic E</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Topic F</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>
      </div>

      <div class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </div>

    </div> <!-- /container -->

"""

create_page(page)

