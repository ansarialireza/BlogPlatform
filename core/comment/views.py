# comments/views.py

from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Comment
from blog.models import Post

class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comments/comment_form.html'
    fields = ['content']
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_id"] = self.kwargs['post_id']
        return context
    

# حذف کامنت
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    success_url = reverse_lazy('blog:post-list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.success_url = reverse_lazy('blog:post-detail', kwargs={'pk': obj.post.pk})
        return obj