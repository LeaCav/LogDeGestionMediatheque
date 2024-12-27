from django.template import loader
from django.http import HttpResponse
from librarian.models import Book, DVD, CD, BoardGame

def media_list(request):
    books = Book.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    games = BoardGame.objects.all()
    template = loader.get_template("members/media_list.html")
    context = {
        'books': books, 'dvds': dvds, 'cds': cds, 'games': games
    }
    return HttpResponse(template.render (context, request))
