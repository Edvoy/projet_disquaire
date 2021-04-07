'''
Une vue est une fonction Python acceptant une requête Web et renvoyant une réponse Web.
Cette réponse peut contenir le contenu HTML d’une page Web, une redirection,
une erreur 404, un document XML, une image… ou vraiment n’importe quoi d’autre.

La vue elle-même contient la logique nécessaire pour renvoyer une réponse.
'''

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Album, Artist, Contact, Booking

def index(request):
# request albums
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    context = {
        'album': albums
        }
    return render(request, 'store/index.html', context)

def listing(request):
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 9)
    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)
    context = {
        'albums': albums,
        'paginate': True
    }
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
    context = {
    'album_title': album.title,
    'artists_name': artists_name,
    'album_id': album.id,
    'thumbnail': album.picture

    }
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)

    if not albums.exists():
        albums = Album.objects.filter(artists__name__icontains=query)
    
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)