from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_blocked = models.BooleanField(default=False)

    def can_borrow(self):
        return not self.is_blocked and sum (self.borrowed_cd.count(), self.borrowed_dvd.count(), self.borrowed_book.count()) < 3