from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Oferta(models.Model):
    tytul = models.CharField(max_length=80)
    tresc = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Oferty"

    def __str__(self):
        return self.tytul + '_' + self.autor.username
