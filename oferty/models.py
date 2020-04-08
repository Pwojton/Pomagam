from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

TYP_POMOCY = (
    ('NM','Nauka do matury'),
    ('NS','Nauka do sprawdzianu'),
    ('NL','Nauka do lekcji'),
)

TYP_OGLOSZENIA = (
    ('SP', 'Szukam pomocy'),
    ('OP', 'Oferuję pomoc'),
)

PRZEDMIOT = (
    ('P','Polski'),
    ('M','Matematyka'),
    ('F','Fizyka'),
    ('I','Informatyka'),
    ('A','Angielski'),
)


class Oferta(models.Model):
    tytul = models.CharField(max_length=80)
    tresc = models.TextField()
    przedmiot = models.CharField(choices=PRZEDMIOT, max_length=1)
    typ_ogloszenia = models.CharField(choices=TYP_OGLOSZENIA, max_length=2)
    typ_pomocy = models.CharField(choices=TYP_POMOCY, max_length=2)
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Oferty"

    def __str__(self):
        return self.tytul + '_' + self.autor.username

	def get_absolute_url(self):
        return reverse('oferta_szczegoly', kwargs={'pk': self.pk})

class Komentarz(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    tresc = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Komentarze"

    def get_absolute_url(self):
        return reverse('komentarz_utworz', kwargs={'pk': self.pk})

    def __str__(self):
        return self.tresc 
