from django.urls import path
from . import views


urlpatterns = [
    path("image/", views.ImageUpload.as_view(), name="Image-view-create"),
    path("view/images/<str:img_id>", views.SpecificDisplayImage.as_view(), name = "Display-image"),
    path("gallery/<str:event_id>", views.EventGallery.as_view(), name = "Gallery-image"),

]