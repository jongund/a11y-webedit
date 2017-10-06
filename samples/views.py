from django.shortcuts import render

def show_all_samples(request):
	return render(request, 'samples/all_samples.html');

