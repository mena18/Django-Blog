from django.urls import path
from .views import *
from .feeds import LatestPostFeed

app_name="blog"
# or  namespace='blog') inside the url to that file


urlpatterns = [
    path('', post_list,name="post_list"),
    path('tag/<slug:tag_slug>/', post_list,name="post_list_by_tag"),
    #path('', PostList.as_view(),name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', post_detail,name="post_detail"),
    path('share/<int:post_id>', post_share,name="post_share"),
    path('feed/',LatestPostFeed(),name='post_feed'),
    path('search/', post_list, name='post_search'),
    path('subs/', add_subscriber, name='subs'),
    
]
