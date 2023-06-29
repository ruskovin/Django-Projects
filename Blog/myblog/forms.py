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
        
        def __init__(self, *args, **kwargs):
            super(CreateArticleForm, self).__init__(*args, **kwargs)
<<<<<<< HEAD
            self.fields['image'].required = False
            
class SearchForm(forms.Form):
    query = forms.CharField()
=======
            self.fields['image'].required = False
>>>>>>> 1c44ffbeda1912d53719e815e941f187747bbc49
