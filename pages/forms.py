from django import forms
from .models import Page
from .models import Tag
from accounts.models import Profile
# from codemirror import CodeMirrorTextarea
from django.utils.crypto import get_random_string
from djangocodemirror.widgets import CodeMirrorWidget
from djangocodemirror.fields import CodeMirrorField


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['useCodeMirror']
        useCodeMirror = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hidden'}))


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['user', 'title', 'description', 'slug', 'public', 'sample', 'assignment', 'tags', 'htmlHead',
                  'htmlBody', 'css', 'javascript']

    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all(),
                                          required=False)


class PageFormWithCodeMirror(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['user', 'title', 'description', 'slug', 'public', 'sample', 'assignment', 'tags', 'htmlHead',
                  'htmlBody', 'css', 'javascript']

    htmlHead = CodeMirrorField(required=False, config_name='html')
    htmlBody = CodeMirrorField(required=False, config_name='html')
    css = CodeMirrorField(required=False, config_name='css')
    javascript = CodeMirrorField(required=False, config_name='javascript')
    tags = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all(),
                                          required=False)
