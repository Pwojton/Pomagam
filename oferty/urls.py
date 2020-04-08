from django.urls import path
from . import views
from .views import OfertaDetailView, OfertaCreateView, OfertaUpdateView, OfertaDeleteView,\
                   KomentarzCreateView, KomentarzUpdateView, KomentarzDeleteView

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('oferta/<int:pk>', OfertaDetailView.as_view(), name='oferta_szczegoly'),
    path('oferta/nowa', OfertaCreateView.as_view(), name='oferta_utworz'),
    path('oferta/<int:pk>/aktualizuj', OfertaUpdateView.as_view(), name='oferta_aktualizuj'),
    path('oferta/<int:pk>/usun', OfertaDeleteView.as_view(), name='oferta_usun'),
    path('post/<int:pk>/komantarz', KomentarzCreateView.as_view(), name='komentarz_utworz'),
    path('post/<int:pk>/komantarz/aktualizuj', KomentarzUpdateView.as_view(), name='komentarz_aktualizuj'),
    path('post/<int:pk>/komantarz/usun', KomentarzDeleteView.as_view(), name='komentarz_usun'),
]