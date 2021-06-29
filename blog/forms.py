from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["guest_name", "guest_email", "comment"]
        labels = {
            "guest_name": "Your Name",
            "guest_email": "Your Email"
        }