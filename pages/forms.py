from django import forms

class PageForm(forms.Form):
	title = forms.CharField(label="title",max_length=30)
	description = forms.CharField(label="description",max_length=200)
	headHTML = forms.CharField()
	bodyHTML = forms.CharField()
	css = forms.CharField()
	javascript = forms.CharField()