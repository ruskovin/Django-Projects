from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    