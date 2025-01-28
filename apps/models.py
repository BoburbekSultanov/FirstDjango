from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField, DecimalField


# Create your models here.


class Jobs(Model):
    nema = CharField(max_length=255)
    address = CharField(max_length=255)
    country = CharField(max_length=255)





class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    title = CharField(max_length=255)
    price = DecimalField(max_digits=12, decimal_places=2)
    description = CharField(max_length=255)
    image = ImageField(upload_to='products/', null=True, blank=True)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='products')

    def __str__(self):
        return self.name