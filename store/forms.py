from django import forms
from .models import Store, Comment


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["title", "content", "buysell", "cost", "type", "image", "thumbnail"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
