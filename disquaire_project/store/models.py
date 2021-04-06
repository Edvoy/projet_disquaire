'''
Il contient les champs et le comportement essentiels des données que vous stockez.
Généralement, chaque modèle correspond à une seule table de base de données.
https://docs.djangoproject.com/fr/3.1/topics/db/models/
'''

from django.db import models

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]