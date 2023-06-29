from typing import Any, Optional, Type
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
<<<<<<< HEAD
from .forms import LoginForm, RegisterForm, CreateArticleForm, SearchForm
=======
from .forms import LoginForm, RegisterForm, CreateArticleForm
>>>>>>> 1c44ffbeda1912d53719e815e941f187747bbc49
from .models import Article
# Create your views here.

class HomeView(ListView, View):
    model = Article
    template_name = 'articles/index.html'
    ordering = '-date_created'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
<<<<<<< HEAD
        context['search'] = SearchForm()
        return context

# def index(request):
#     articles = Article.objects.order_by('-date_created')
#     context ={
#         'articles':articles,
#         'username':request.user.username,
#     }
#     return render(request, 'articles/index.html', context)
=======
        return context

def index(request):
    articles = Article.objects.order_by('-date_created')
    context ={
        'articles':articles,
        'username':request.user.username,
    }
    return render(request, 'articles/index.html', context)
>>>>>>> 1c44ffbeda1912d53719e815e941f187747bbc49




def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':RegisterForm
        }
    return render(request, 'register.html', context)


class Login(LoginView):
    template_name='login.html'
    redirect_authenticated_user = True
    authentication_form = LoginForm
    next_page = 'articles/index.html'
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        return render(request,self.template_name, context={'form':form})
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)    

class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = "articles/create-article.html"
    success_url = ''
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(post)
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    
class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'articles/article-confirm-delete.html'
    success_url = reverse_lazy('home')
    
class UpdateArticleView(UpdateView):
    model = Article
    template_name = 'articles/update-article.html'
    success_url = reverse_lazy('home')
    fields = ['title','image', 'content']
<<<<<<< HEAD
    queryset = Article.objects.all()
    
def searchView(request):
    query = request.GET.get('query')
    results = Article.objects.filter(title__icontains='query')
    form = SearchForm
    return render(request,'articles/search-article.html',{'results':results, "form":form})
=======
    queryset = Article.objects.all()
>>>>>>> 1c44ffbeda1912d53719e815e941f187747bbc49
