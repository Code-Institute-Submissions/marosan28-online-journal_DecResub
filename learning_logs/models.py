from django.db import models


class Topic(models.Model):
    """Topic the user is interested in."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a model"""
        return self.text