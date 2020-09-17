from django.db import models

class Place(models.Model):
  place = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  also_known_as = models.CharField(max_length=50)
  as_seen_in = models.CharField(max_length=200)
  pestilence = models.CharField(max_length=200)
  danger_level = models.IntegerField()
  image = models.CharField(max_length=300)

def __str__(self):
    return f'{self.place} - {self.country}' 
