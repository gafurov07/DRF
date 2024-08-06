from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, SlugField, Model, TextField, IntegerField, ForeignKey, CASCADE, DateTimeField, \
    ImageField, IntegerChoices
from django.utils.text import slugify


class CustomModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Category(CustomModel):
    pass


class Product(CustomModel):
    description = TextField()
    price = IntegerField()
    discount = IntegerField()
    category = ForeignKey('apps.Category', CASCADE)
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)




class User(AbstractUser):
    pass


class ProductImage(Model):
    product = ForeignKey('apps.Product', CASCADE)
    image = ImageField(upload_to='product/')
