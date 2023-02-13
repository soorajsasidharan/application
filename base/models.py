from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="user-default.png")
    bio = models.TextField(blank=True, null=True, default= " . ")

    

    def __str__(self):
        return str(self.user)

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Home(models.Model):
    
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    post_image = models.ImageField(upload_to='post')
    caption = models.TextField(blank=True )
   

    def __str__(self):
        return str(self.username)
