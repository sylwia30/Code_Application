from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .forms import CreateCommentForm
from .models import Post, Comment


class PostListView(LoginRequiredMixin, View):

    def get(self, request):
        posts = Post.objects.all().order_by('-date_posted')
        create_comment = CreateCommentForm()
        return render(request, 'chat/chat.html', {'posts': posts,
                                                   'create_comment': create_comment
                                                  })

    # def post(self, request):
    #     created_comment = CreateCommentForm(request.POST)
    #     posts = Post.objects.all().order_by('-date_posted')
    #     if created_comment.is_valid():
    #         get_comment = created_comment.cleaned_data.get('text')
    #         post_id = int(request.POST.get("post_id"))
    #         save_comment = Comment(text=get_comment, user=request.user, post_id=post_id)
    #         save_comment.save()
    #         messages.success(request, "Your comment has been added!")
    #         create_comment = CreateCommentForm()
    #         return render(request, 'chat/chat.html', locals())