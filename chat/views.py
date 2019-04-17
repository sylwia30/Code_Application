from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404

from .forms import CreateCommentForm
from .models import Post, Comment



class PostListView(ListView):
    model = Post
    template_name = 'chat/chat.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('chat')

    def form_valid(self, form):
        form.instance.author = self.request.user # czy autor równa sie zalogowanemu użytkownikowi
        return super().form_valid(form)


class UserPostView(ListView):
    model = Post
    template_name = 'chat/user_posts.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        create_comment = CreateCommentForm()
        return render(request, 'chat/post_detail.html', {'post': post,
                                                   'create_comment': create_comment})
    def post(self, request, pk):
        created_comment = CreateCommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if created_comment.is_valid():
            get_comment = created_comment.cleaned_data.get('text')
            save_comment = Comment(text=get_comment, user=request.user, post=post)
            save_comment.save()
            messages.success(request, "Twój komentarz został dodany!")
            create_comment = CreateCommentForm()
            return render(request, 'chat/post_detail.html', locals())


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'chat/post_update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    """ poniższa funkcja wyklucza edytowanie postów przez innych użytkowników, zwraca 403 Forbidden """

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False











# class PostListView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         posts = Post.objects.all().order_by('-date_posted')
#         create_comment = CreateCommentForm()
#         return render(request, 'chat/chat.html', {'posts': posts,
#                                                    'create_comment': create_comment
#                                                   })

    # def post(self, request):
    #     created_comment = CreateCommentForm(request.POST)
    #     posts = Post.objects.all().order_by('-date_posted')
    #     if created_comment.is_valid():
    #         get_comment = created_comment.cleaned_data.get('text')
    #         post_id = int(request.POST.get("post_id"))
    #         save_comment = Comment(text=get_comment, user=request.user, post_id=post_id)
    #         save_comment.save()
    #         messages.success(request, "Twój komentarz został dodany!")
    #         create_comment = CreateCommentForm()
    #         return render(request, 'chat/chat.html', locals())