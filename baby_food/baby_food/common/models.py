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
