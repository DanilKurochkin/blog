from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    posts = Post.objects.order_by('-date')
    count = posts.count()
    paginated_posts = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginated_posts.get_page(page_number)
    
    return render(request, 'blog/blog.html', {'page_obj' : page_obj, 'count' : count})

def detail(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    
    return render(request, 'blog/detail.html', {'post' : post})