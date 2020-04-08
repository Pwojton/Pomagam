from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Oferta, Komentarz
from django.views.generic import ListView, DetailView, CreateView,\
                                UpdateView, DeleteView

def glowna(request):
    lista = Oferta.objects.all().order_by('-data')
    paginator = Paginator(lista, 1)
    strona = request.GET.get('page')

    try:
        oferty = paginator.page(strona)
    except PageNotAnInteger:
        oferty = paginator.page(1)
    except EmptyPage:
        oferty = paginator.page(paginator.num_pages)

    context = {
    	'oferty': oferty
    }

    return render(request, 'oferty/strona_glowna.html', context)

class OfertaDetailView(DetailView):
    model = Oferta

    def get_context_data(self, **kwargs):
        context = super(OfertaDetailView, self).get_context_data(**kwargs)
        context['komentarze'] = Komentarz.objects.filter(oferta=self.kwargs.get('pk'))
        return context


class OfertaCreateView(LoginRequiredMixin, CreateView):
    model = Oferta
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class OfertaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Oferta
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        oferta = self.get_object()
        if self.request.user == oferta.autor:
            return True
        return False


class OfertaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Oferta
    success_url = '/'

    def test_func(self):
        oferta = self.get_object()
        if self.request.user == oferta.autor:
            return True
        return False


class KomentarzCreateView(LoginRequiredMixin, CreateView):
    model = Komentarz
    fields = ['tresc']

    def form_valid(self, form, **kwargs):
        oferta = get_object_or_404(Oferta, pk=self.kwargs.get('pk'))
        form.instance.autor = self.request.user
        form.instance.oferta = oferta
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        pk = self.object.oferta.pk
        return reverse('oferta_szczegoly', kwargs={'pk': pk})


class KomentarzUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Komentarz
    fields = ['tresc']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        komentarz = self.get_object()
        if self.request.user == komentarz.autor:
            return True
        return False

    def get_success_url(self, **kwargs):
        pk = self.object.oferta.pk
        return reverse('oferta_szczegoly', kwargs={'pk': pk})


class KomentarzDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Komentarz

    def get_success_url(self, **kwargs):
        pk = self.object.oferta.id
        return reverse('oferta_szczegoly', kwargs={'pk': pk})

    def test_func(self):
        komentarz = self.get_object()
        if self.request.user == komentarz.autor:
            return True
        return False

