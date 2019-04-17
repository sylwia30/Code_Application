from django.urls import path
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     UserPostView,
# )
from .views import PostListView, PostCreateView, UserPostView, PostDetailView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('chat/', PostListView.as_view(), name='chat'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>/', UserPostView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]