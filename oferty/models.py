from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Oferta(models.Model):
    tytul = models.CharField(max_length=80)
    tresc = models.TextField()
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
