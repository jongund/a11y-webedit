from django import forms
from .models import Page
from .models import Tag
from codemirror import CodeMirrorTextarea
from django.utils.crypto import get_random_string

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = ['user', 'title', 'description', 'slug', 'public', 'sample', 'assignment', 'tags', 'htmlHead', 'htmlBody', 'css', 'javascript']

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

	tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Tag.objects.all(),
	required=False)

