from django.shortcuts import render
from .models import Page
from .forms import PageForm

# Create your views here.

def index(request):
	p = Page(title="Title",description="Description")
	context = {
	'p' : p,
	}
	return render(request, 'pages/index.html', context)
	
def update_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PageForm()

    return render(request, 'index.html', {'form': form})