from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.



# WatchList Model
class WatchList(models.Model):
    
    title = models.CharField(max_length=50)
    storyline = models.TextField()
    active = models.BooleanField(default = True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        
        return self.title
    
    
        

# StreamPlatform Model
class StreamPlatform(models.Model):
    
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField()
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        
        return self.name


# Review Model

class Review(models.Model):
    
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.TextField()
    active = models.BooleanField(default = True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    
    
    def __str__(self):
        return f'{str(self.rating)} {self.description}'