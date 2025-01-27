from django.db .models import Model
from django.db.models import CharField


# Create your models here.


class Jobs(Model):
    nema = CharField(max_length=255)
    address = CharField(max_length=255)
    country = CharField(max_length=255)

