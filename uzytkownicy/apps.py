from django.apps import AppConfig


class UzytkownicyConfig(AppConfig):
    name = 'uzytkownicy'
    
    def ready(self):
        import uzytkownicy.signals 
