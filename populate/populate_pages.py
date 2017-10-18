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

from django.core.exceptions   import ObjectDoesNotExist
from pages.models import Page
from pages.models import Tag
from django.contrib.auth.models import User



def create_page(page):

  try:
    p = Page.objects.get(webKey=page.webKey, user=admin_user)
    print("Update Page: " + page.webKey)

    p.title       = page.title
    p.description = page.description
    p.htmlHead    = page.htmlHead
    p.htmlBody    = page.htmlBody
    p.sample      = page.sample
    p.public      = page.public
    p.javascript  = page.javascript
    p.css         = page.css

  except ObjectDoesNotExist:
    print("Create Page: " + page.webKey)
    p = Page(user=admin_user, webKey= page.webKey, title=page.title, description=page.description, htmlHead = page.htmlHead, htmlBody=page.htmlBody, sample=page.sample, public=page.public, javascript=page.javascript, css=page.css)

  p.save()
  p.tags.remove()
  p.save()

  for t in page.tags.split(' '):
    try:
      tag = Tag.objects.get(slug=t)
      p.tags.add(tag)
      p.save()
      print('Tag added: ' + tag.title)
    except ObjectDoesNotExist:
      print('Tag not found: ' + tag)

# Page.objects.all().delete()

admin_user = User.objects.get(username=settings.ADMIN_USERNAME)

page = type("myobj",(object,),dict(webKey='', title='', description='', htmlHead='', htmlBody='', css='', javascript='', tags='', sample=False, public=True))

page.webKey = 'structure-problem-1'
page.title = 'Problem 1: Using role attributes to create ARIA landmarks'
page.description = 'Problem 1 for Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = True

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
           Problem 1: Using <code>role</code> attribute to create landmarks
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

page.webKey = 'structure-problem-2'
page.title = 'Problem 2: Using HTML5 sectioning elements to create ARIA landmarks'
page.description = 'Problem 2 for Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = True

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
           Problem 2: Using HTML5 Sectioning Elements to create Landmarks
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


page.webKey = 'structure-solution-1'
page.title = 'Solution 1: Landmarks defined using role attribute'
page.description = 'Solution for Problem 1 for Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""
page.tags = 'structure'
page.sample = True
page.public = False


page.htmlBody = """
    <div class="container">
      <div role="banner">
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
      </div>

      <div role="main">
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Solution 1: Landmark Roles Defined Using Role Attribute
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
      </div>

      <div class="well" role="contentinfo">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </div>

    </div> <!-- /container -->

"""

create_page(page)

page.webKey = 'structure-solution-2'
page.title = 'Solution 2: Landmarks defined using HTML5 sectioning elements'
page.description = 'Solution for Problem 2: Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""
page.tags = 'structure'
page.sample = True
page.public = False


page.htmlBody = """
    <div class="container">
      <header>
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
      </header>

      <main>
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Solution 2: Landmark Roles Defined Using Role Attribute
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
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>

    </div> <!-- /container -->

"""

create_page(page)

page.webKey = 'structure-problem-3'
page.title = 'Problem 3: Identifying and properly nesting headings on a page'
page.description = 'Problem 3 for Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = True

page.htmlBody = """
    <div class="container">
     <header>
        <div class="header clearfix">
          <nav>
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
          </nav>
        </div>

        <div class="jumbotron">
          <h1 class="display-3">ARIA Landmarks, Headings and page Titles</h1>
          <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
        </div>
      </header>

      <main>
        <div class="row">
          <div class="col-sm-12">
             <h2>
             Add Proper Heading Sructure to this Page
             </h2>
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
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>


    </div> <!-- /container -->
"""

create_page(page)

page.webKey = 'structure-solution-3'
page.title = 'Solution 3: Identifying and properly nesting headings on a page'
page.description = 'Solution for problem 3: Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = False


page.htmlBody = """
    <div class="container">
      <header>
        <div class="header clearfix">
          <nav>
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
          </nav>
        </div>

        <div class="jumbotron">
          <h1 class="display-3">ARIA Landmarks, Headings and page Titles</h1>
          <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
        </div>
      </header>

      <main>
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Add Proper Heading Sructure to this Page
             </h1>
          </div>
        </div>

        <div class="row marketing">

          <div class="col-sm-6">
            <h2>Topic A</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic B</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic C</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>

          <div class="col-sm-6">
            <h2>Topic D</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic E</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic F</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>
        </div>
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>

    </div> <!-- /container -->
"""

page.css = """
  h2 {
    font-size: 135%;
  }
"""

create_page(page)

page.webKey = 'structure-problem-4'
page.title = 'Problem 4: Adding a skip-to-main content link'
page.description = 'Problem 4 for Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = True


page.htmlBody = """
    <div class="container">
      <header>
        <div class="header clearfix">
          <nav>
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
          </nav>
        </div>

        <div class="jumbotron">
          <h1 class="display-3">ARIA Landmarks, Headings and page Titles</h1>
          <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
        </div>
      </header>

      <main>
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Add Proper Heading Sructure to this Page
             </h1>
          </div>
        </div>

        <div class="row marketing">

          <div class="col-sm-6">
            <h2>Topic A</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic B</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic C</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>

          <div class="col-sm-6">
            <h2>Topic D</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic E</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic F</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>
        </div>
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>

    </div> <!-- /container -->
"""

page.css = """
  h2 {
    font-size: 135%;
  }
"""

create_page(page)

page.webKey = 'structure-solution-4a'
page.title = 'Solution 4a: Adding a skip-to-main content link using simple skip link'
page.description = 'Solution for problem 4: Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = False


page.htmlBody = """
    <div class="container">
      <header>
        <a class="btn btn-default" href="#main" onfocus="showElement(event)" onblur="hideElement(event)">Skip to main content</a>
        <div class="header clearfix">
          <nav>
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
          </nav>
        </div>

        <div class="jumbotron">
          <h1 class="display-3">ARIA Landmarks, Headings and page Titles</h1>
          <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
        </div>
      </header>

      <main><a id="main" name="main"></a>
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Add Proper Heading Sructure to this Page
             </h1>
          </div>
        </div>

        <div class="row marketing">

          <div class="col-sm-6">
            <h2>Topic A</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic B</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic C</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>

          <div class="col-sm-6">
            <h2>Topic D</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic E</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic F</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>
        </div>
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>

    </div> <!-- /container -->
"""

page.css = """
  h2 {
    font-size: 135%;
  }

  a[href="#main"] {
    position: absolute;
    top: -30em;
    left: -300em;
    background-color: #ddd;
    color: #333;
    z-index: 1000;
  }

"""
page.javascript = """

function showElement(event) {

  event.currentTarget.style.left = "0";
  event.currentTarget.style.top  = "0";

}

function hideElement(event) {

  event.currentTarget.style.left = "-300em";
  event.currentTarget.style.top  = "-30em";

}


"""


create_page(page)

page.webKey = 'structure-solution-4b'
page.title = 'Solution 4b: Adding a skip-to-main content link using SkipTo,js'
page.description = 'Solution for problem 4: Landmarks, Headings, Page Titles and Navigation badging course.'
page.htmlHead = """
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" type="text/javascript"></script>
"""

page.tags = 'structure'
page.sample = True
page.public = False


page.htmlBody = """
     <div class="container">
      <header>
        <div class="header clearfix">
          <nav>
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
          </nav>
        </div>

        <div class="jumbotron">
          <h1 class="display-3">ARIA Landmarks, Headings and page Titles</h1>
          <p class="lead">Cras justo odio, dapibus ac facilisis in, egestas eget quam. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
        </div>
      </header>

      <main>
        <div class="row">
          <div class="col-sm-12">
             <h1>
             Add Proper Heading Sructure to this Page
             </h1>
          </div>
        </div>

        <div class="row marketing">

          <div class="col-sm-6">
            <h2>Topic A</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic B</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic C</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>

          <div class="col-sm-6">
            <h2>Topic D</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

            <h2>Topic E</h2>
            <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

            <h2>Topic F</h2>
            <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
          </div>
        </div>
      </main>

      <footer class="well">
        <p>&copy; University of Illinois 2017 | <a href="#">Privacy</a> | <a href="#">Facebbok</a> | <a href="#">Accessibility</a></p>
      </footer>

    </div> <!-- /container -->

    <script>
    var skipToConfig =
    {
      "settings": {
        "skipTo": {
          "headings"     : "h1, h2, h3, h4",
          "main"         : "main, [role=main]",
          "landmarks"    : "[role=navigation], [role=search]",
          "accesskey"    : "0",
          "wrap"         : "true",
          "visibility"   : "onfocus",
        }
      }
    };
    </script>
    <script type="text/javascript" src="http://paypal.github.io/skipto/downloads/js/SkipTo.min.js"></script>
"""

page.css = """
  h2 {
    font-size: 135%;
  }
"""

create_page(page)
