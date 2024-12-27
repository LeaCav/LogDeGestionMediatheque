from django.contrib import admin
from .models import Book, DVD, CD, BoardGame

admin.site.register(Book)
admin.site.register(DVD)
admin.site.register(CD)
admin.site.register(BoardGame)