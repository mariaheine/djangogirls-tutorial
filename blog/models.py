from django.db import models
from django.utils import timezone

# Create your models here.

# models.Model means that the Post is a Django Model, 
# so Django knows that it should be saved in the database.
class Post(models.Model):
    # link to another model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    # text with limited number of characters
    title = models.CharField(max_length=200)

    # long text without limit
    text = models.TextField()

    # date and time
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now
        self.save()

    # Double-check that you use two underscore characters (_) 
    # on each side of str. This convention is used frequently 
    # in Python and sometimes we also call them "dunder" 
    # (short for "double-underscore").
    def __str__(self):
        return self.title
