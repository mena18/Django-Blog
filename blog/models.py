from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.



status_choices = {
    ('draft','Draft'),
    ('published','Published'),
}

class Published(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")




class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=status_choices,default='draft')

    tags = TaggableManager()

    objects = models.Manager() # The default manager.
    published = Published() # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       kwargs={"year":self.publish.year,
                             "month":self.publish.month,
                             "day":self.publish.day,
                             "post": self.slug})



class Comment(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = "comments")
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    body = models.TextField()

    parent_comment = models.ForeignKey('Comment',null=True,on_delete=models.CASCADE,related_name='sub_comments',blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        if(parent_comment):
            return "Commet by {} on {}".format(self.name,self.parent_comment)    
        return "Commet by {} on {}".format(self.name,self.post)



class SubScribers(models.Model):
    emails = models.CharField(max_length=100)
    name = models.CharField(max_length=100)











