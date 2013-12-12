from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Thing(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug =  models.SlugField()
    content = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return('blog',[self.slug])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-time']

# admin.site.register(Thing)

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

admin.site.register(Category)
admin.site.register(Page)


class UserProfile(models.Model):
    #from djano.contrib.auth.models import User
    #This line is required, it linksed to the User model
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images',blank=True)

    def __unicode__(self):
        return self.user.username 

admin.site.register(UserProfile)

class MyModel(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

admin.site.register(MyModel)