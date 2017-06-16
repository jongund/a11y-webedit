from django import forms
from .models import Page
from codemirror import CodeMirrorTextarea
from django.utils.crypto import get_random_string

class PageForm(forms.ModelForm):
	class Meta: 
		model = Page
		fields = "__all__"
	htmlHead = forms.CharField(widget= CodeMirrorTextarea(
		mode = "xml"), required = False,
		)
	htmlBody = forms.CharField(widget= CodeMirrorTextarea(
		mode = "xml"), required = False,
		)
	css = forms.CharField(widget= CodeMirrorTextarea(
		mode = "css"), required = False,
		)
	javascript = forms.CharField(widget= CodeMirrorTextarea(
		mode = "javascript"), required = False,
		)