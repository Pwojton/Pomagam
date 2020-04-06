from django.shortcuts import render
from .models import Oferta


def glowna(request):
    context = {
    'oferty': Oferta.objects.all()
    }

    return render(request, 'oferty/strona_glowna.html', context)

