from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from .models import Restaurant

def map_view(request):
    """Hiển thị bản đồ với các quán ăn."""
    return render(request, 'restaurants/map.html')

def restaurant_json(request):
    """API trả về dữ liệu quán ăn dạng JSON cho bản đồ."""
    data = []
    for r in Restaurant.objects.all():
        data.append({
            "id": r.id,
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

class RestaurantDetailView(DetailView):
    """Hiển thị trang chi tiết quán ăn."""
    model = Restaurant
    template_name = 'restaurants/restaurant_detail.html'
    context_object_name = 'restaurant'
