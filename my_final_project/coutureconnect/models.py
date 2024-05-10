from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 



class coutureconnect(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class testclass(models.Model):
  name = models.CharField(max_length=255)
  phoneNumber = models.IntegerField()
  email = models.EmailField(max_length=254)

# class Service(models.Model):
#     name = models.CharField(max_length=200)
#     # Additional fields for the Service

class Review(models.Model):
    # reviewer = models.ForeignKey(User, related_name="reviewer_reviews", on_delete=models.CASCADE)
    # reviewee = models.ForeignKey(User, related_name="reviewee_reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)  

class Event(models.Model):
    name = models.CharField(max_length=100)
    event_time = models.DateTimeField(default=timezone.now)  # Uses timezone-aware datetime
