from django.shortcuts import render
from blog.models import Blog


def all_blogs(request):
    """Собираем все объекты модели и отображаем на странице"""
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
