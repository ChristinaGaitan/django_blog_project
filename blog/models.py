from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  author = models.ForeignKey("auth.User", verbose_name='author', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now())
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.publish_date = timezone.now()
    self.save()

  def approve_comments(self):
    return self.comments.filter(approve_comment=True)

  def get_absolute_url(self):
    return reverse("post_detail", kwargs={"pk": self.pk})

  def __str__(self):
    return self.title

class Comment(models.Model):
  author = models.ForeignKey("blog.Post", related_name='comments', verbose_name='author', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now())
  approve_comment = models.BooleanField(default=False)

  def approve(self):
    self.approve_comment = True
    self.save()

  def get_absolute_url(self):
    return reverse("post_list")

  def __str__(self):
    return self.text
