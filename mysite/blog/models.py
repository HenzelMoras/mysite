from django.db import models
from django.utils import timezone  # for time related objects like publish, created, updated
from django.contrib.auth.models import User  # to be used to link the users to author using foreign key 
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')  # get Posts with published status


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

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)  # reverse ordering filtered using publish object for displaying the latest posts

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return self.title                          