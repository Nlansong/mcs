from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


#Create your models here.
class UserProfile(models.Model):
    options = [
        ('brother','brother'),
        ('sister','sister'),
        ('pastor','pastor'),
        ('Deacon','Deacon'),
        ('Deaconess','Deaconess'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50,choices=options)
    username = models.CharField(max_length=200)
    profile_picture = models.ImageField(default="")
    phone_number = models.PositiveIntegerField(null=True)
    birthday =models.DateTimeField(null=True, blank=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=160, null=True, blank=True)
    


    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
    @receiver(post_save, sender=user)
    def save_user(sender, instance, **kwargs):
        instance.userprofile.save()