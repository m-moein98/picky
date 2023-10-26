from django.urls import path

from fruit.views import json_serializer_view

urlpatterns = [
    path("", json_serializer_view, name="fruits"),
    path("<int:id>", json_serializer_view, name="fruits"),
]
