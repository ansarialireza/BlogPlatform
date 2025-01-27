from rest_framework import viewsets
from blog.models import Post
from .serializers import PostSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
