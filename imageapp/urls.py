from django.urls import path,include
from .views import imageGalleryViewSet
from rest_framework import routers


'''
Added a router for urls. 
http://127.0.0.1:8080/imagegallery -> shows all items in storted order of creation. oldest first
http://127.0.0.1:8080/imagegallery/all -> shows all items in storted order of creation. latest first
http://127.0.0.1:8080/imagegallery/Category2/ -> shows the images in a particular category. latest first
'''

router = routers.DefaultRouter()
router.register(r'imagegallery',imageGalleryViewSet)

urlpatterns = [path('', include(router.urls))]