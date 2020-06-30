from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image
from django.core.mail import send_mail




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

    objects = models.Manager() #  default manager.
    published = Published() #  custom manager.

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



    def save(self):
        super().save()
        img = Image.open(self.image.path)
        output_size = (600,300)
        img.thumbnail(output_size)
        img.save(self.image.path)


        try:
            subscribers = SubScribers.objects.all()
            for sub in subscribers:
                subject = f"New Post from the blog ({self.title})"
                body = f"Hi {sub.name} Read our new post {self.title}\n{self.body[0:30]}\n\n You can read more from here http://127.0.0.1:8000{self.get_absolute_url()}"
                send_mail(subject,body,'blog@gmail.com',[sub.emails])
        except :
            pass

        









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
        if(self.parent_comment):
            return "Commet by {} on {}".format(self.name,self.parent_comment)    
        return "Commet by {} on {}".format(self.name,self.post)



class SubScribers(models.Model):
    emails = models.CharField(max_length=100)
    name = models.CharField(max_length=100)











# post signal when post is created 
# create/edit/delete posts as write
# allow user to register in the blog and only registerd users  receive messages and comment
# compress images
# allow edit and delete for comments and sub comments
# allow tagging other people 
# improve search 
# allow search by tags
# add about me section
# allow replying only by clicking on a button next to a person
# learn  to use django forms with ajax
# learn to send data back with forms when failure happen 




