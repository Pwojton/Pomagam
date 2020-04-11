from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RejestracjaFormularz, AktualizacjaProfiluFormularz, AktualizacjaUżytkownikaFormularz
from django.contrib.auth.decorators import login_required


def zarejestruj(request):
    if request.method == 'POST':
        formularz = RejestracjaFormularz(request.POST)
        if formularz.is_valid():
            formularz.save()
            username = formularz.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}! Twoje konto zostało utworzone. Możesz się teraz zalogować')
            return redirect('zaloguj')
    else:
        formularz = RejestracjaFormularz()
    return render(request, 'uzytkownicy/rejestracja.html', {'form': formularz})


@login_required
def profil(request):
    if request.method == 'POST':
        u_form = AktualizacjaUżytkownikaFormularz(request.POST, instance=request.user)
        p_form = AktualizacjaProfiluFormularz(request.POST, request.FILES, instance=request.user.profil)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Informacje zostały zaktualizowane!')
            return redirect('profil')

    else:
        u_form = AktualizacjaUżytkownikaFormularz(instance=request.user)
        p_form = AktualizacjaProfiluFormularz(instance=request.user.profil)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'uzytkownicy/profil.html', context)



def profil_innego_uzytkownika(request, pk):
    profil = User.objects.get(pk=pk)
     return render(request, 'uzytkownicy/profil_innego_uzytkownika.html', {'uzytkownik': profil})
