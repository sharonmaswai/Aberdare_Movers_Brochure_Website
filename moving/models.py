from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):

    name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email = models.EmailField(max_length=200)
  
    def savecontact(self):
        self.save()
        
    
   
    def __str__(self):
        return self.bio
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length=500)

    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    
def __str__(self):
    return self.image_name        