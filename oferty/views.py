from django.shortcuts import render

oferty = [
    {
        'autor': 'ZbrSnd',
        'tytul': 'Pomoc z matmy',
        'tresc': 'Treść',
        'data': 'Marzec 20, 2020',
    },
    {
        'autor': 'Pwojton',
        'tytul': 'Pomoc z matmy',
        'tresc': 'Treść',
        'data': 'Marzec 20, 2020',}

]

def glowna(request):
    context = {
        'oferty': oferty
    }

    return render(request, 'oferty/strona_glowna.html', context)
