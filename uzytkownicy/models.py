from django.contrib.auth.models import User
from django.db import models
from PIL import Image
import os

KLASY = (
    ('IA', 'IA'),
    ('IIA', 'IIA'),
    ('IIIA', 'IIIA'),
    ('IB', 'IB'),
    ('IIB', 'IIB'),
    ('IIIB', 'IIIB'),
    ('IC', 'IC'),
    ('IIC', 'IIC'),
    ('IIIC', 'IIIC'),
    ('ID', 'ID'),
    ('IID', 'IID'),
    ('IIID', 'IIID'),
    ('IE', 'IE'),
    ('IIE', 'IIE'),
    ('IIIE', 'IIIE'),
    ('IF', 'IF'),
    ('IIF', 'IIF'),
    ('IIIF', 'IIIF'),
)


def ustaw_nazwe(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.username, ext)
    return os.path.join('zdjecia_profili', filename)
    

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
	zdjecie = models.ImageField(default='zdjecie.png', upload_to=ustaw_nazwe)
    klasa = models.CharField(choices=KLASY, max_length=4)
    numer_telefonu = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profil, self).save(*args, **kwargs)

        img = Image.open(self.zdjecie.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.zdjecie.path)
