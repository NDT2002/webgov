# forms.py
from django import forms
from .models import Post
from .models import Term
from .models import User
from . import models
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content', 'post_date', 'post_author', 'post_status', 'post_type','featured_image']

        
class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['name', 'slug', 'term_group']


class TermTaxonomyForm(forms.ModelForm):
    class Meta:
        model= models.TermTaxonomy
        fields=['term','taxonomy']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_login', 'user_pass', 'user_email', 'display_name']