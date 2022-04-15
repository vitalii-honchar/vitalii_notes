from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.BlogPostView.as_view(), name='blog_post'),
    path('login/', views.BlogLogin.as_view(), name='login')
]
