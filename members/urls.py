from django.urls import path
from members.views import media_list

urlpatterns = [
    path("media", media_list, name="liste des médias"),
]
