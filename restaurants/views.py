from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant

def map_view(request):
    return render(request, 'restaurants/map.html')

def restaurant_json(request):
    data = []
    for r in Restaurant.objects.all():
        data.append({
            "name": r.name,
            "address": r.address,
            "phone": r.phone,
            "image": r.image.url if r.image else "",
            "open_time": r.open_time.strftime("%H:%M"),
            "close_time": r.close_time.strftime("%H:%M"),
            "latitude": float(r.latitude),
            "longitude": float(r.longitude),
            "rating": float(r.rating),
        })
    return JsonResponse(data, safe=False)
