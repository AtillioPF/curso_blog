from django.shortcuts import render
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