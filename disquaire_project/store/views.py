'''
Une vue est une fonction Python acceptant une requête Web et renvoyant une réponse Web.
Cette réponse peut contenir le contenu HTML d’une page Web, une redirection,
une erreur 404, un document XML, une image… ou vraiment n’importe quoi d’autre.

La vue elle-même contient la logique nécessaire pour renvoyer une réponse.
'''

from django.http import HttpResponse

from .models import ALBUMS

def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)

def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)