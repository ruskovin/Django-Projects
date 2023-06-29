from django.urls import path
from .views import PostListView, PostDetail

app_name = "myblog"
urlpatterns =[
    path('',PostListView.as_view(), name='api_post_list'),
    path('<int:pk>', PostDetail.as_view(), name ='api_detail'),
]