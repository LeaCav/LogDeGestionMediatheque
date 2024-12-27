from django.urls import path
from librarian.views import add_member, member_list, media_list, borrow_media

urlpatterns = [
    path("ajouter_membre", add_member, name="ajouter un membre"),
    path("membre", member_list, name="liste des membres"),
    path("media", media_list, name= "liste des medias"),
    path("emprunt", borrow_media, name= "emprunts"),
]