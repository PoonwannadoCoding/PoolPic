from rest_framework import serializers
from .models import Image



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        #["img_id", "event_id", "publisher_id", "published_date", "file"]