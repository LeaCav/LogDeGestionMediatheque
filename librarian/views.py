from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Book, DVD, CD, BoardGame
from members.models import Member
from .create_media.forms import MediaForm
from .create_member.forms import MemberForm, ModifMemberForm

# Formulaire pour ajouter un membre
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form=MemberForm()
    template = loader.get_template("librarian/add_member.html")
    context = {
        'form' : form
    }
    return HttpResponse(template.render (context, request))

# Formulaire pour modifier un membre
def modif_member(request):
    if request.method == 'POST':
        form = ModifMemberForm(request.POST)
        if form.is_valid():
            obj_id = form.cleaned_data['id']
            obj:Member = get_object_or_404(Member, id=obj_id)
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            form.save()
            return redirect('member_list')
        else:
            form=ModifMemberForm()
        template = loader.get_template("librarian/add_member.html")
    context = {
        'form' : form
    }
    return HttpResponse(template.render (context, request))

# Liste des membres
def member_list(request):
    members = Member.objects.all()
    template = loader.get_template("librarian/member_list.html")
    context = {
        'members' : members
    }
    return HttpResponse(template.render (context, request))

# Afficher la liste des médias
def media_list(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=MediaForm()
    books = Book.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    games = BoardGame.objects.all()
    template = loader.get_template("librarian/media_list.html")
    context = {
        'books': books, 'dvds': dvds, 'cds': cds, 'games': games, 'form' : form
    }
    return HttpResponse(template.render (context, request))

# Créer un emprunt
def borrow_media(request):
    template = loader.get_template("librarian/borrow_media.html")
    context = {

    }
    return HttpResponse(template.render (context, request))