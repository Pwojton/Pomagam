#Aplikacja Pomagam

Uruchomienie lokalne projektu

git clone https://github.com/Pwojton/Pomagam.git

python -m venv venv

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser
