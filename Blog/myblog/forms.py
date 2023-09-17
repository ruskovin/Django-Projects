from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Article

#forms here

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
        widgets ={
            'username': forms.TextInput(attrs={'placeholder':"password"}),
            'password': forms.TextInput(attrs={'type':'password', 'placeholder':"password"})
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username','email','password1','password2']
        
    

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author',)
        widgets = {
            'title': forms.TextInput(attrs={"class":'input'})
        }
        
        def __init__(self, *args, **kwargs):
            super(CreateArticleForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = False
            
class SearchForm(forms.Form):
    query = forms.CharField()
