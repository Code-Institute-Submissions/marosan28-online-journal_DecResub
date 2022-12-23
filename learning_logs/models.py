from django.db import models
from django import forms


class Topic(models.Model):
    """Topic the user is interested in."""
    text = models.CharField(max_length=200)
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


class EntryModelForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']

        
class EmailAddress(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name']
        widgets = {
            'topic_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    topic_name = forms.CharField(max_length=250, validators=[validate_non_numeric, validate_special_characters],label ='')




