from django.db import models 
from django.utils import timezone


class Post(models.Model):
#new class called Post belongs to models.Model
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
	#Text length
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
		#define

    def __str__(self):
	#define
        return self.title