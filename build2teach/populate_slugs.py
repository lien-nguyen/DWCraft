from blog.models import Post
from django.utils.text import slugify

for post in Post.objects.all():
    if not post.slug:
        post.slug = slugify(post.title)
        post.save()
print("Slugs populated.")