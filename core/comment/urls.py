from django.urls import path
from .views import CommentListView, CommentCreateView, CommentDeleteView

app_name = 'comment'

urlpatterns = [
    path('post/<int:post_id>/comments/', CommentListView.as_view(), name='comment-list'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]