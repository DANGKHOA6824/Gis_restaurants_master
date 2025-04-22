from django.db import migrations
from datetime import time

def create_restaurants(apps, schema_editor):
    Restaurant = apps.get_model('restaurants', 'Restaurant')
    data = [
        {
            "name": "Cua Cốm Restaurant",
            "address": "21 Phân Khu Nam, Tân An, Long An",
            "phone": "0889999929",
            "image": "restaurant_images/cuacom.jpg",
            "open_time": time(10, 30),
            "close_time": time(1, 0),
            "latitude": 10.536612,
            "longitude": 106.413001,
            "rating": 4.6
        },
        {
            "name": "Samba Restaurant",
            "address": "60 Nguyễn Văn Tạo, Tân An, Long An",
            "phone": "0834550066",
            "image": "restaurant_images/samba.jpg",
            "open_time": time(9, 0),
            "close_time": time(23, 45),
            "latitude": 10.534900,
            "longitude": 106.417600,
            "rating": 4.5
        },
        {
            "name": "Cá Chèo Bẻo Hotpot & BBQ",
            "address": "B4-35, Đường 8, Lavila Green City, Tân An, Long An",
            "phone": "0939182711",
            "image": "restaurant_images/cheobeo.jpg",
            "open_time": time(10, 30),
            "close_time": time(23, 0),
            "latitude": 10.532700,
            "longitude": 106.420900,
            "rating": 4.4
        },
        {
            "name": "Bún Đậu Mẹt Long An",
            "address": "32 Nguyễn Đình Chiểu, Tân An, Long An",
            "phone": "0901234567",
            "image": "restaurant_images/bundaumet.jpg",
            "open_time": time(9, 0),
            "close_time": time(21, 0),
            "latitude": 10.540000,
            "longitude": 106.415500,
            "rating": 4.2
        },
        {
            "name": "Bò Sốt Hẻm",
            "address": "19 Nguyễn Thái Bình, Tân An, Long An",
            "phone": "0902345678",
            "image": "restaurant_images/boso them.jpg",
            "open_time": time(10, 0),
            "close_time": time(22, 0),
            "latitude": 10.537500,
            "longitude": 106.422200,
            "rating": 4.3
        },
        {
            "name": "Ngói Đất BBQ & Lẩu",
            "address": "28 Nguyễn Văn Rành, Tân An, Long An",
            "phone": "0903456789",
            "image": "restaurant_images/ngo idat.jpg",
            "open_time": time(16, 0),
            "close_time": time(23, 0),
            "latitude": 10.538800,
            "longitude": 106.418800,
            "rating": 4.4
        },
        {
            "name": "The Pizza Company",
            "address": "20 Nguyễn Đình Chiểu, Tân An, Long An",
            "phone": "19006066",
            "image": "restaurant_images/pizza.jpg",
            "open_time": time(10, 0),
            "close_time": time(22, 0),
            "latitude": 10.539200,
            "longitude": 106.415700,
            "rating": 4.1
        },
        {
            "name": "Jisan - Bếp Trà Truyền Thống",
            "address": "45 Nguyễn An Ninh, Tân An, Long An",
            "phone": "0912345678",
            "image": "restaurant_images/jisan.jpg",
            "open_time": time(8, 0),
            "close_time": time(22, 0),
            "latitude": 10.535900,
            "longitude": 106.416800,
            "rating": 4.5
        },
        {
            "name": "Hào Ái Quán",
            "address": "18 Nguyễn Văn Rành, Tân An, Long An",
            "phone": "0904567890",
            "image": "restaurant_images/haoai.jpg",
            "open_time": time(9, 0),
            "close_time": time(22, 0),
            "latitude": 10.538400,
            "longitude": 106.418000,
            "rating": 4.0
        },
        {
            "name": "Bình Mi Tuấn Map Sài Gòn",
            "address": "25 Nguyễn Văn Rành, Tân An, Long An",
            "phone": "0905678901",
            "image": "restaurant_images/binhmituan.jpg",
            "open_time": time(7, 0),
            "close_time": time(21, 0),
            "latitude": 10.538900,
            "longitude": 106.419200,
            "rating": 4.2
        },
    ]
    for item in data:
        Restaurant = apps.get_model('restaurants', 'Restaurant')
        Restaurant.objects.create(**item)

class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_restaurants),
    ]
