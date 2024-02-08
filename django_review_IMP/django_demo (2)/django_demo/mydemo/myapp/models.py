from django.db import models

# Create your models here.   
class Review(models.Model):
    username = models.CharField(max_length=200)
    rating = models.IntegerField()
    category = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    
    def __str__(self):
       
        return self.company