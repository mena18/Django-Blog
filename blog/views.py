from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailForm,CommentForm,SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity,SearchVector, SearchQuery, SearchRank

# Create your views here.


def post_list(request,tag_slug=None):
    tag=None
    if(tag_slug==None):
        posts = Post.published.all()
    else:
        tag = get_object_or_404(Tag,slug=tag_slug)
        posts = Post.published.filter(tags__in = [tag])

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

    context = {'page':page,'posts':posts,'tag':tag}
    return render(request,'blog/post_list.html',context)




class PostList(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 2
    queryset = Post.published.all()



def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,publish__day=day,publish__month=month,publish__year=year)

    tags_id = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=tags_id).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    context={'post':post,'comments':post.comments.all(),'similar_posts':similar_posts}
    if(request.method=='POST'):
        form = CommentForm(request.POST);
        comment = form.save(commit = False)
        comment.post = post
        comment.save()
        context['new_comment'] = True
    else:
        form = CommentForm();

    context['form']=form
    return render(request,"blog/post_detail.html",context);




def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')
    sent=False

    if(request.method=="POST"):
        form = EmailForm(request.POST)
        if(form.is_valid()):
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject ="{} recomed you to see {}".format(form.cleaned_data['name'],post.title)
            body = "You can Reat the Post here {}\n\n {}\n{}\n\n{}".format(post_url,form.cleaned_data['name'],form.cleaned_data['email_from'],form.cleaned_data['comment'])
            send_mail(subject,body,'admin@gmail.com',[form.cleaned_data['email_to']])
            sent = True
        else:
            print("form is not valid")
    else:
        form = EmailForm()

    context = {'form':form,'sent':sent,'post':post}
    return render(request,"blog/share.html",context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.filter(title__contains=query)


    return render(request,
                  'blog/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
