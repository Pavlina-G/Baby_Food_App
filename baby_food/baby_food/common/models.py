from django.db import models

# class Location(models.Model):
#     pass


class Gallery(models.Model):

    picture = models.ImageField(
        upload_to='recipe_pics',
    )

    upload_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.picture.name

    class Meta:
        verbose_name_plural = 'Gallery'


class Location(models.Model):

    city = models.CharField(
        max_length=20,
        default='Burgas',
        # editable=False,
    )

    address = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return f'{self.city}, {self.address}'