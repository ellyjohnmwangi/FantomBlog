from django.shortcuts import render
from .models import Post, Category
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.

class IndexView(ListView):
    template_name = "posts/index.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context
