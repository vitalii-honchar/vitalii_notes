from django.views import generic
from .models import BlogPost
from django.views import generic

from .models import BlogPost


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blog_post_list"

    def get_queryset(self):
        return BlogPost.objects.order_by('-published_date')


class BlogPostView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_post.html'
