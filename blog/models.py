from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)     


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    body = models.TextField()
    picture = models.ImageField(blank=True, upload_to='post_images')
    ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, related_name='blog_posts')
    category = models.ForeignKey(Category, related_name='posts')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)     

    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                                     args=[self.created.year, 
                                                 self.created.strftime('%m'), 
                                                 self.created.strftime('%d'), 
                                                 self.slug])


class Comment(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 

    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User, related_name='blog_comments')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)                                                                                  