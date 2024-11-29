from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['data', 'content_body',]
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Enter your comment here...'})
        }