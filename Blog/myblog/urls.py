from django.urls import path
from .views import Login, registerView, index, CreateArticleView, DeleteArticleView, UpdateArticleView, HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
# urlconf here

urlpatterns = [
    # path("", index, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("register", registerView , name="register"),
    path('login', Login.as_view() , name="login"),
    path('logout', LogoutView.as_view(next_page="login"), name="logout"),
    path('create-article',CreateArticleView.as_view(), name='create-article' ),
    path('update-article/<int:pk>',UpdateArticleView.as_view(), name='update-article' ),
    path('delete-article/<int:pk>',DeleteArticleView.as_view(), name='delete-article' ),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
