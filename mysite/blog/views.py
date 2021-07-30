from django.shortcuts import get_object_or_404, render
from .models import Post
"""
request =  o que entra (o que o navegador envia)
response = o que o computador/server onde o programa esta responde para o navegador
"""
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blog/post_list.html',
        {'post_list':posts}
    )

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {'post':post}
    )

def contacts(request):
    return render(
        request,
        'blog/contacts.html',
        {}
    )

def about(request):
    return render(
        request,
        'blog/about.html',
        {}
    )