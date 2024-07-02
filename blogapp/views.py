from django.http import Http404
from django.shortcuts import get_object_or_404, render
from blogapp.models import Post,Category,Tags
from django.db import models

# Create your views here.
def blog(request):
    blogposts = Post.objects.filter(published= True)
    
    #blog categories
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    
    #recent blogs
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    
    #tags
    blog_tags = Tags.objects.all()
    
    context = {
        'blogposts':blogposts,
        'blog_categories':blog_categories,
        'recent_blogs':recent_blogs,
        'blog_tags':blog_tags
        }
    return render(request,'blog.html',context)


def blog_details(request,url):
    post = get_object_or_404(Post,url=url)
    
    #blog categories
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    
    #recent blogs
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    
    #tags
    blog_tags = Tags.objects.all()
    context = {
        "post":post,
        'blog_categories':blog_categories,
        'recent_blogs':recent_blogs,
        'blog_tags':blog_tags
        }
    return render(request,'single.html',context)



def post_list_by_category(request,category_url):
    try:
        selected_blog_category = Category.objects.get(url=category_url)
        blogposts = Post.objects.filter(published= True,category=selected_blog_category)
        
        
            #blog categories
        blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
        
        
        #recent blogs
        recent_blogs = Post.objects.order_by('-created_at')[:3]
        
        
        #tags
        blog_tags = Tags.objects.all()
    except Category.DoesNotExist:
        message = "That category does not exist"
        return render(request,'errors.html',{"message":message})
        
    context = {
        'blogposts':blogposts,
        'blog_categories':blog_categories,
        'recent_blogs':recent_blogs,
        'blog_tags':blog_tags
        }
    
    return render(request,'blog.html',context)


def post_list_by_tags(request,tag_url):
    try:
        selected_blog_tag = Tags.objects.get(url=tag_url)
        blogposts = Post.objects.filter(published= True,tags=selected_blog_tag)
            #blog categories
        blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
        
        
        #recent blogs
        recent_blogs = Post.objects.order_by('-created_at')[:3]
        
        
        #tags
        blog_tags = Tags.objects.all()
    except Tags.DoesNotExist:
        message = "That Tag does not exist"
        return render(request,'errors.html',{"message":message})
        
    context = {
        'blogposts':blogposts,
        'blog_categories':blog_categories,
        'recent_blogs':recent_blogs,
        'blog_tags':blog_tags
        }
    
    return render(request,'blog.html',context)



def blog_search(request):
    query = request.GET.get('q')
    if query:
        blogposts = Post.objects.filter(title__icontains=query,published=True)
    else:
        blogposts=None
        
    #blog categories
    blog_categories = Category.objects.annotate(blog_count=models.Count('post'))
    
    
    #recent blogs
    recent_blogs = Post.objects.order_by('-created_at')[:3]
    
    
    #tags
    blog_tags = Tags.objects.all()
    
    context = {
        'blogposts':blogposts,
        'blog_categories':blog_categories,
        'recent_blogs':recent_blogs,
        'blog_tags':blog_tags
        }
    
    return render(request,'blog.html',context)
        
        