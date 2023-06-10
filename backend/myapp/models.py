from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    books = models.ManyToManyField('myapp.Book', related_name='authors', blank=True, null=True)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

    def total_price(self):
        return sum(self.get_queryset().values_list('price', flat=True))

    def publish(self, model_instance):
        model_instance.is_published = True
        model_instance.save()

    def bulk_publish_false(self, model_qts):
        model_qts.update(is_published=False)

    def bulk_publish_true(self, model_qts):
        model_qts.update(is_published=True)

class Book(models.Model):
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    author2 = models.ManyToManyField('myapp.Author', related_name='books2', blank=True, null=True)

    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='media/', blank=True, null=True)



    def __str__(self):
        return self.title

