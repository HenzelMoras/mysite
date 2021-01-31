from django.db import models
from django.utils import timezone  # for time related objects like publish, created, updated
from django.contrib.auth.models import User  # to be used to link the users to author using foreign key 
# Create your models here.


class Post(models.Model):
    STATUS_CHOICES =(
        ('draft','Draft'),
        ('published','Published'),  # Choices used for 'updated' object
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,  # if The author is deleted remove all related posts too
                               related_name='blog_posts')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # default published time is set to now
    created = models.DateTimeField(auto_now_add=True)   # created object is always set to now
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                               choices=STATUS_CHOICES,   # status with choices
                              default='draft')

    class Meta:
        ordering = ('-publish',)  # reverse ordering filtered using publish object for displaying the latest posts

    def __str__(self):
        return self.title                           