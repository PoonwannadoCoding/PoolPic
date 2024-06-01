from django.db import models

# Create your models here.

def image_dir_path(instance,filename):
    return "uploads/{0}/{1}".format(instance.event_id,filename)

class Image(models.Model):
    img_id = models.AutoField(primary_key=True)
    event_id = models.CharField(max_length=25)
    publisher_id = models.CharField(max_length=25)
    published_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=image_dir_path)


    def __str__(self) -> str:
        return self.img_id