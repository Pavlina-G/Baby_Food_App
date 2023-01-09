from django.db import models

# class Location(models.Model):
#     pass


class Gallery(models.Model):

    picture = models.ImageField(
        upload_to='recipe_pics',
    )