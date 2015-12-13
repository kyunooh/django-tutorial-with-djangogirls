from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


# param: HttpRequset instance
# return: HttpResponse instance
def index(request):
    # QuerySet
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })


def post_detail(request, pkl):
    # Post.DoesNotExist
    post = get_object_or_404(Post, pk=pkl)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })
