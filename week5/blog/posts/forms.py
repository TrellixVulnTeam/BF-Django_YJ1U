from django import forms
from .models import Post, Comment

class TitleForm(forms.Form):
    title = forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'message')