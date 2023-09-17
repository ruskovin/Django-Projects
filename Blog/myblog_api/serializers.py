from rest_framework import serializers
from myblog.models import Article

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"