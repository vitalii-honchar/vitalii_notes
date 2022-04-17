from django.views import generic
from .models import BlogPost
from .forms import LoginForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import views as auth_views

from .models import BlogPost


class IndexView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blog_post_list'
    login_url = 'blog:login'
    permission_required = 'blog.view_blogpost'

    def get_queryset(self):
        return BlogPost.objects.order_by('-published_date')


class BlogPostView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_post.html'
    login_url = 'blog:login'
    permission_required = 'blog.view_blogpost'


class BlogLogin(auth_views.LoginView):
    next_page = 'blog:index'
    form_class = LoginForm


class BlogLogout(auth_views.LogoutView):
    template_name = 'registration/login.html'
    next_page = 'blog:login'
