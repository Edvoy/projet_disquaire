'''
Une vue est une fonction Python acceptant une requête Web et renvoyant une réponse Web.
Cette réponse peut contenir le contenu HTML d’une page Web, une redirection,
une erreur 404, un document XML, une image… ou vraiment n’importe quoi d’autre.

La vue elle-même contient la logique nécessaire pour renvoyer une réponse.
'''

from django.http import HttpResponse

from .models import Album, Artist, Contact, Booking

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)

    if not albums.exists():
        message = "Misère de misère, nous n'avons trouvé aucun résultat !"
    else:
        albums = ["<li>{}</li>".format(album.title) for album in albums]
        message = """
            Nous avons trouvé les albums correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format("</li><li>".join(albums))

    return HttpResponse(message)