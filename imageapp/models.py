from django.db import models

# Create your models here.
IMAGE_CATEGORY = (('Category1', 'Category1'),
                  ('Category2', 'Category2'),
                  ('Category3', 'Category3'),
                  ('Category4', 'Category4'))

# class with a drop down to choose category
# and button to upload image
class imageGallery(models.Model):
    imageCategory = models.CharField(choices=IMAGE_CATEGORY, max_length=20, default='1')
    imageContent = models.ImageField(upload_to='static/images', default=None)

