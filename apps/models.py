
from django.db.models import Model, ForeignKey, CASCADE, ImageField, TextChoices
from django.db.models.fields import CharField, DecimalField, IntegerField


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
    main_image = ImageField(upload_to='products/', null=True, blank=True)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Image(Model):
    class ImageType(TextChoices):
        XS = 'xs', 'Xs'
        S = 's', 'S'
        M = 'm', 'M'
        L = 'l', 'L'
        XL = 'xl', 'Xl'
        XXL = 'xxl', 'Xxl'
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')
    size = CharField(max_length=255, choices=ImageType)



class Tariff(Model):
    class StatusType(TextChoices):
        MONTH = 'month', 'Month'
        YEAR = 'year', 'Year'
    name = CharField(max_length=255)
    price = DecimalField(max_digits=5, decimal_places=2)
    discount = IntegerField(max_length=3)
    time = CharField(max_length=255, choices=StatusType.choices, default=StatusType.MONTH) # noqa

    def __str__(self):
        return self.name






# class Job(Model):
#     class StatusType(TextChoices):
#         FULL_TIME = 'full time', 'Full time'
#         REMOTE = 'remote', 'Remote'
#         CONTRACT = 'contract', 'Contract'
#         WFH = 'wfh', 'WFH'
#
#     name = CharField(max_length=100)
#     address = CharField(max_length=100)
#     country = CharField(max_length=100)
#     status = CharField(max_length=255, choices=StatusType.choices, default=StatusType.REMOTE)