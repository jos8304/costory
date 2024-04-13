from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label="Title")
    content = forms.CharField(label="content", widget=forms.Textarea)
