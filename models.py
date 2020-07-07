from django.db import models

class categories(models.Model):

     
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField() 
    offer = models.BooleanField(default=False)

    def __str__(self):

        return self.name