from rest_framework import generics
from myblog.models import Article
from .serializers import PostSerializer
# Create your views here.

class PostListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostSerializer
