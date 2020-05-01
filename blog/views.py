from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
# Create your views here.


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {'page':page,'posts':posts}
    return render(request,'blog/post_list.html',context)




class PostList(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 2
    queryset = Post.published.all()



def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,publish__day=day,publish__month=month,publish__year=year)
    context = {'post':post}
    return render(request,"blog/post_detail.html",context);
