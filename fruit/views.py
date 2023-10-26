from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Fruit
import json
from django.core.cache import cache


def json_serializer_view(request, id=None):
    if request.method == "GET":
        if id is not None:
            cache_key = f"Fruit_{id}"
            cached_data = cache.get(cache_key)
            if cached_data:
                obj: Fruit = cached_data
            else:
                obj = get_object_or_404(Fruit, pk=id)
            data = {
                "id": obj.id,
                "name": obj.name,
                "calories": obj.calories,
            }
            return JsonResponse(data)
        else:
            queryset = Fruit.objects.all()
            data = [
                {"id": obj.id, "name": obj.name, "calories": obj.calories}
                for obj in queryset
            ]
            return JsonResponse(data)

    elif request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name", "")
        calories = data.get("calories", "")
        new_obj = Fruit(name=name, calories=calories)
        new_obj.save()
        cache_key = f"Fruit_{new_obj.id}"
        cache.set(cache_key, new_obj, timeout=None)
        response_data = {
            "id": new_obj.id,
            "name": new_obj.name,
            "calories": new_obj.calories,
        }
        return JsonResponse(response_data, status=201)
