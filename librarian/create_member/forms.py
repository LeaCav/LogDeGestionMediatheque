from django import forms
from members.models import Member

# Création du formulaire d'ajout de membre
class MemberForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label="Nom")
    email = forms.CharField(max_length=255, required=True, label="Email")
    
    def save(self):
        name = self.cleaned_data[
            'name'
        ]
        email = self.cleaned_data[
            'email'
        ]
        return Member.objects.create(name=name, email=email)
    
# Modifier un membre
class ModifMemberForm(forms.ModelForm):
    id = forms.IntegerField(label="id", required=True)
    class Meta:
        model = Member
        fields = ['id', 'name', 'email']
        labels = {
            'id': 'id',
            'name': 'Nom',
            'email': 'Email'
        }