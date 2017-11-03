from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=True)
    post_text = models.CharField(max_length=2000, blank=True)
    pub_date = models.DateTimeField('date published')
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.post_text

@python_2_unicode_compatible
class Talk(models.Model):
    talk_username = models.CharField(max_length=50, blank=True)
    post = models.ForeignKey(Post)
    talk_text = models.CharField(max_length = 200, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.talk_text
