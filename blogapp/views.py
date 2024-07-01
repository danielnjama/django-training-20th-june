from django.shortcuts import get_object_or_404, render
from blogapp.models import Post,Category,Tags

# Create your views here.
def blog(request):
    blogposts = Post.objects.filter(published= True)
    print(blogposts)
    
    context = {
        "blogposts":blogposts
        }
    return render(request,'blog.html',context)


def blog_details(request,url):
    post = get_object_or_404(Post,url=url)
    context = {"post":post}
    return render(request,'single.html',context)