from django.db import models
from members.models import Member

class Media(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    borrower = models.ForeignKey(
        Member, null=True, blank=True, on_delete=models.SET_NULL, related_name='borrowed_%(class)s'
    )
    borrow_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True 