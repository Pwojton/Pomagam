from django.shortcuts import render


def glowna(request):
    return render(request, 'oferty/strona_glowna.html')
