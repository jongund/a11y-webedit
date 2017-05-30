from django.shortcuts import render
from .models import Page
from .forms import PageForm
from django.http import HttpResponse

# Create your views here.

def index(request):
	p = Page(title="Title",description="Description")
	
	if request.method == 'POST':
		form=PageForm(request.POST)
		#create form instance and populate with form data
		if form.is_valid():
			form.save()
			return HttpResponse("Thanks!")
			
	else:
		form=PageForm()
		
	context = {
	'p' : p,
	'form' : form,
	}
	
	return render(request, 'pages/index.html', context)

	

	