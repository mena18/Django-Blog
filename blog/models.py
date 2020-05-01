from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
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
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=status_choices,default='draft')


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
