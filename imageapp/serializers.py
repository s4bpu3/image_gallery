from rest_framework import serializers
from .models import imageGallery


# using a model serializer to serialize imageGallery objects. Shows both fields of the object
class imageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = imageGallery
        fields = '__all__'
