from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer
# Create your views here.


class ImageUpload(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class SpecificDisplayImage(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'img_id'

class EventGallery(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Image.objects.filter(event_id=event_id)
