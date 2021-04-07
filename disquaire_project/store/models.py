'''
Il contient les champs et le comportement essentiels des données que vous stockez.
Généralement, chaque modèle correspond à une seule table de base de données.
https://docs.djangoproject.com/fr/3.1/topics/db/models/
'''

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
      return self.name
class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)
    
    def __str__(self):
        return self.title
class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
      return self.contact.name