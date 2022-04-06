from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  Computetion (models.Model):
    image = models.ImageField(upload_to = "image_uploaded", null = True, blank = True)
    video = models.FileField(upload_to = "video_uploaded", null = True)
    date_uploaded = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)