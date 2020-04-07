from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RejestracjaFormularz
from django.contrib.auth.decorators import login_required


def zarejestruj(request):
    if request.method == 'POST':
        formularz = RejestracjaFormularz(request.POST)
        if formularz.is_valid():
            formularz.save()
            username = formularz.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}! Twoje konto zostało utworzone. Możesz się teraz zalogować')
            return redirect('glowna')
    else:
        formularz = RejestracjaFormularz()
    return render(request, 'uzytkownicy/rejestracja.html', {'form': formularz})


@login_required
def profil(request):
    return render(request, 'uzytkownicy/profil.html') 
