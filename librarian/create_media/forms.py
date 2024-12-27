from django import forms
from librarian.models import Book, CD, DVD, BoardGame

# Création du formulaire d'ajout de média
class MediaForm(forms.Form):
    MEDIA_TYPE = [
        ('book', 'Book'),
        ('cd', 'CD'),
        ('dvd', 'DVD'),
        ('boardGame', 'BoardGame')
    ]
    media_type = forms.ChoiceField(choices=MEDIA_TYPE, label="Type de média")
    title = forms.CharField(max_length=255, required=True, label="Titre")
    author = forms.CharField(max_length=255, required=True, label="Auteur (livres)")
    artist = forms.CharField(max_length=255, required=True, label="Artiste (CD)")
    director = forms.CharField(max_length=255, required=True, label="Réalisateur (DVD)")
    creator = forms.CharField(max_length=255, required=True, label="Editeur (jeux)")

    def save(self):
        media_type = self.cleaned_data[
            'media_type'
        ]
        title = self.cleaned_data[
            'title'
        ]
        if media_type == 'book':
            return Book.objects.create(title=title, author=self.cleaned_data['author'])
        elif media_type == 'cd':
            return CD.objects.create(title=title, artist=self.cleaned_data['artist'])
        elif media_type == 'dvd':
            return DVD.objects.create(title=title, director=self.cleaned_data['director'])
        elif media_type == 'boardGame':
            return BoardGame.objects.create(title=title, creator=self.cleaned_data['creator'])