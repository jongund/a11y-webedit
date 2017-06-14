from django import forms
from .models import Page
from codemirror import CodeMirrorTextarea

class PageForm(forms.ModelForm):
	class Meta: 
		model = Page
		fields = "__all__"
	htmlHead = forms.CharField(widget= CodeMirrorTextarea(
		mode = "xml", theme="cobalt"), required = False,
		)
	htmlBody = forms.CharField(widget= CodeMirrorTextarea(
		mode = "html"), required = False,
		)
	css = forms.CharField(widget= CodeMirrorTextarea(
		mode = "css"), required = False,
		)
	javascript = forms.CharField(widget= CodeMirrorTextarea(
		mode = "javascript"), required = False,
		)
	