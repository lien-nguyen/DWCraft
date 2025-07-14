from django.shortcuts import render
from .models import Post
import markdown 
from django.utils.safestring import mark_safe

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        post.content_html = mark_safe(markdown.markdown(post.content, extensions=['fenced_code', 'codehilite']))
    return render(request, 'blog/post_list.html', {'posts': posts})