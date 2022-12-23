from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from .models import Topic, Entry
import re

def validate_non_numeric(value):
    if value.isnumeric():
        raise forms.ValidationError("Topic cannot be numerical only.")

def validate_special_characters(value):
    if re.search(r'[^a-zA-Z0-9]', value):
        raise forms.ValidationError("Special characters are not allowed.")

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        widgets = {
            'topic_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    topic_name = forms.CharField(max_length=250, validators=[validate_non_numeric, validate_special_characters],label ='')


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")


