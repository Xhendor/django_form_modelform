from django import forms
from .models import Post


class ContactForm(forms.Form):
  from_email = forms.EmailField(required=True)
  subject = forms.CharField(required=True)
  message = forms.CharField(widget=forms.Textarea, required=True)


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content',)
