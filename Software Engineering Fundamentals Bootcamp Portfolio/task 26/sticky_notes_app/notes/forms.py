from django import forms
from .models import StickyNote


# Class for the form that appears when adding or editing a note
class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['title', 'description']
