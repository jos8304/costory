from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.
class Post(models.Model):
    #title, content, create_date,updated_date
    title = models.CharField(max_length=50, unique=True, error_messages={'unique': 'This title already exists.'})
    content = models.TextField(validators=[MinLengthValidator(10, 'Please write at least 10 characters.'), validate_symbols])
    dt_created = models.DateField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateField(verbose_name="Date Modified", auto_now=True)

    def __str__(self):
        return self.title
    