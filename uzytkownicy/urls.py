from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('zarejestruj/', views.zarejestruj, name='zarejestruj'),
    path('profil/', views.profil, name='profil'),
    path('profil/<int:pk>', views.profil_innego_uzytkownika, name='profil_innego_uzytkownika'),
    path('zaloguj/', auth_views.LoginView.as_view(template_name='uzytkownicy/zaloguj.html'), name='zaloguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(template_name='uzytkownicy/wyloguj.html'), name='wyloguj'),
