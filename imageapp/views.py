# from django.shortcuts import render
from .models import imageGallery
from rest_framework import viewsets
from .serializers import imageGallerySerializer
from rest_framework.response import Response

'''
http://127.0.0.1:8080/imagegallery -> shows all items in storted order of creation. oldest first
http://127.0.0.1:8080/imagegallery/all -> shows all items in storted order of creation. latest first
http://127.0.0.1:8080/imagegallery/Category2/ -> shows the images in a particular category. latest first
'''


# Create your views here.
class imageGalleryViewSet(viewsets.ModelViewSet):
    queryset = imageGallery.objects.all()
    serializer_class = imageGallerySerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        params_list = params['pk']
        try:
            # detailed view. It shows the details of a particular image
            params_list = int(params_list)
            queryset = imageGallery.objects.get(id=int(params_list))
            serializer = imageGallerySerializer(queryset)
        except:
            # Show all items if filter all
            if params_list == 'all':
                # sort items in the order of creation. Latest first
                queryset = imageGallery.objects.all().order_by('-id')
            # filter by category. Latest first
            else:
                queryset = imageGallery.objects.filter(imageCategory=params_list).order_by('-id')
            # show the list of items that matches the criteria
            serializer = imageGallerySerializer(queryset, many=True)
        return Response(serializer.data)
