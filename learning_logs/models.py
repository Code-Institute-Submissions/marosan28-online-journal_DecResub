from django.db import models
from django import forms
import re

def validate_non_numeric(value):
    if value.isnumeric():
        raise forms.ValidationError("Topic cannot be numerical only.")

def validate_special_characters(value):
    if re.search(r'[^a-zA-Z0-9]', value):
        raise forms.ValidationError("Special characters are not allowed.")

class Topic(models.Model):
    """Topic the user is interested in."""
    text = models.CharField(max_length=200, validators=[validate_non_numeric, validate_special_characters])
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a model"""
        return self.text


class Entry(models.Model):
    """Learning log entries for a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


def non_numeric(value):
    if not any(char.isdigit() for char in value):
        raise forms.ValidationError("Your entry needs to contain at least one numerical character.")

def validate_length(value):
    if len(value) < 50:
        raise forms.ValidationError("Your entry cannot be less than 50 characters.")
    if len(value) > 1000:
        raise forms.ValidationError("Your entry cannot exceed 1000 characters.")

class EntryModelForm(forms.ModelForm):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        validators=[non_numeric, validate_length]
    )

    class Meta:
        model = Entry
        fields = ['text']

        
class EmailAddress(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }