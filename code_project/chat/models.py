from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="tytuł:")
    content = models.TextField(verbose_name="treść:")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # """jak zapisujemy nowy post piszemy poniższą funkcję aby przeniosła nas do
    # post-detail do nowo utworzonego postu"""

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_comment = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

