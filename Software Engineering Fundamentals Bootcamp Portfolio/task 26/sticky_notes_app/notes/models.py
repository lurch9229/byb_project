from django.db import models


# Class for the notes.
class StickyNote(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
