from django.urls import path
from . import views

urlpatterns = [
    path("blog/",views.blog,name='blog'),
    path('blog/<slug:url>/',views.blog_details,name='blog_details'),
]
