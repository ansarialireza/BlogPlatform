from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSeralizer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSeralizer
    
