from django import forms
from .models import Post
from .validators import validate_symbols
from django.core.exceptions import ValidationError



class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content']
    
    def clen_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('* cannot be included.')
        
        return title

