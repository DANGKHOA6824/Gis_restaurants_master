from django.db import migrations
from datetime import time

def create_restaurants(apps, schema_editor):
    Restaurant = apps.get_model('restaurants', 'Restaurant')
    data = [
    {
        "name": "Quán GABI BBQ (Nướng, Lẩu và Bia tươi)",
        "address": "8 Nguyễn Cửu Vân, Phường 4, Tân An, Long An, Việt Nam",
        "phone": "0818226229",
        "image": "restaurant_images/bbq.jpg",
        "open_time": time(10, 30),
        "close_time": time(1, 0),
        "latitude": 10.53186,
        "longitude": 106.40872,
        "rating": 4.2
    },
    {
        "name": "SPICY BOX VINCOM TÂN AN",
        "address": "Góc, Đ. Hùng Vương/đường Mai Thị Tốt, Tân An, Long An, Việt Nam",
        "phone": "0862362936",
        "image": "restaurant_images/spicybox.jpg",
        "open_time": time(9, 0),
        "close_time": time(23, 45),
        "latitude": 10.53445,
        "longitude": 106.41037,
        "rating": 4.6
    },
    {
        "name": "GoGi House Long An",
        "address": "340 Đ. Hùng Vương, Phường 3, Tân An, Long An, Việt Nam",
        "phone": "02727300007",
        "image": "restaurant_images/gogi.jpg",
        "open_time": time(10, 30),
        "close_time": time(23, 0),
        "latitude": 10.53192,
        "longitude": 106.41381,
        "rating": 4.8
    },
    {
        "name": "Ẩm thực Hai Lúa",
        "address": "GCG4+WRJ, Phường 7, Tân An, Long An, Việt Nam",
        "phone": "0855606975",
        "image": "restaurant_images/hailua.jpg",
        "open_time": time(9, 0),
        "close_time": time(21, 0),
        "latitude": 10.52740,
        "longitude": 106.40698,
        "rating": 4.1
    },
    {
        "name": "L'A Steak & Pizza",
        "address": "198 Đ. Hùng Vương, Phường 2, Tân An, Long An, Việt Nam",
        "phone": "0941800938",
        "image": "restaurant_images/pizza.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.537500,
        "longitude": 106.422200,
        "rating": 4.3
    },
    {
        "name": "Phố Ẩm Thực Chay Hương Sen",
        "address": "113 QL62, Phường 2, Tân An, Long An, Việt Nam",
        "phone": "0355222941",
        "image": "restaurant_images/chay.jpg",
        "open_time": time(16, 0),
        "close_time": time(23, 0),
        "latitude": 10.542208724243377,
        "longitude": 106.40375331028588,
        "rating": 4.5
    },
    {
        "name": "Quán Buffet IGO",
        "address": "26a Trịnh Quang Nghị, Phường 4, Tân An, Long An, Việt Nam",
        "phone": "0937031393",
        "image": "restaurant_images/igo.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.539519039423013, 
        "longitude": 106.40109255898673,
        "rating": 4.2
    },
    {
        "name": "Sushi Zen",
        "address": "164 Thủ Khoa Huân, Phường 1, Tân An, Long An 82106, Việt Nam",
        "phone": "0343643737",
        "image": "restaurant_images/shushi.jpg",
        "open_time": time(8, 0),
        "close_time": time(22, 0),
        "latitude": 10.537451657958986, 
        "longitude": 106.41726091484347,
        "rating": 4.5
    },
    {
        "name": "Ốc sơn ca",
        "address": "2 Nguyễn Công Trung, Phường 3, Tân An, Long An, Việt Nam",
        "phone": "0385026227",
        "image": "restaurant_images/oc.jpg",
        "open_time": time(9, 0),
        "close_time": time(22, 0),
        "latitude": 10.532926575481026, 
        "longitude": 106.41940668202439,
        "rating": 4.6
    },
    {
        "name": "Buffet ALO BBQ",
        "address": "63 Nguyễn Minh Trường, Phường 3, Tân An, Long An 82000, Việt Nam",
        "phone": "0848580313",
        "image": "restaurant_images/alo.jpg",
        "open_time": time(7, 0),
        "close_time": time(21, 0),
        "latitude": 10.530395031839214, 
        "longitude": 106.42406299682456,
        "rating": 4.1
    },
    {
        "name": "Quán Bình Minh",
        "address": "58 Nguyễn Trung Trực, Phường 2, Tân An, Long An, Việt Nam",
        "phone": "0946330816",
        "image": "restaurant_images/binhminh.jpg",
        "open_time": time(7, 0),
        "close_time": time(21, 0),
        "latitude": 10.53887298420659, 
        "longitude": 106.40965148790069,
        "rating": 4.1
    },
    {
        "name": "Nhà hàng Beluga",
        "address": "GCCC+9H Tân An, Long An, Việt Nam",
        "phone": "0901112299",
        "image": "restaurant_images/beluga.jpg",
        "open_time": time(8, 0),
        "close_time": time(22, 0),
        "latitude": 10.520954300404778, 
        "longitude": 106.42144516061373,
        "rating": 4.2
    },
    {
        "name": "Quán Cơm Nhà Lá",
        "address": "119 QL1, Phường 2, Tân An, Long An, Việt Nam",
        "phone": "02723829982",
        "image": "restaurant_images/nhala.jpg",
        "open_time": time(9, 0),
        "close_time": time(0, 0),
        "latitude": 10.537716673780759, 
        "longitude": 106.40415698270516,
        "rating": 4.1
    },
    {
        "name": "Há Cảo A Te",
        "address": "189 Đ. Hùng Vương, Phường 3, Tân An, Long An, Việt Nam",
        "phone": "0798929393",
        "image": "restaurant_images/ate.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.5313013221666, 
        "longitude":106.41656813538854,
        "rating": 4.6
    },
    {
        "name": "Bún đậu mắm tôm Quê Nhà",
        "address": "40c Nguyễn Cửu Vân, Phường 4, Tân An, Long An, Việt Nam",
        "phone": "0852020202",
        "image": "restaurant_images/bundau.jpg",
        "open_time": time(6, 0),
        "close_time": time(9, 0),
        "latitude": 10.530140225095998, 
        "longitude": 106.40753388061042,
        "rating": 4.2
    },
    {
        "name": "Quán Lẩu Dê Tám Chín",
        "address": "21 Nguyễn Cửu Vân, Phường 4, Tân An, Long An, Việt Nam",
        "phone": "0949165444",
        "image": "restaurant_images/89.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.530657084075479,
        "longitude":  106.40518426554563,
        "rating": 4.5
    },
    {
        "name": "Sông Quê Quán",
        "address": "28 Lưu Văn Tế, Phường 4, Tân An, Long An 83000, Việt Nam",
        "phone": "0842192192",
        "image": "restaurant_images/songque.jpg",
        "open_time": time(8, 0),
        "close_time": time(22, 0),
        "latitude": 10.536405762946357, 
        "longitude": 106.39750241894055,
        "rating": 4.3
    },
    {
        "name": "Cháo Lòng Rạp Hát",
        "address": "2114 Trà Quý Bình, Phường 2, Tân An, Long An, Việt Nam",
        "phone": "0921883979",
        "image": "restaurant_images/chaolong.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.538863422235083, 
        "longitude": 106.40854239114536,
        "rating": 4.1
    },
    {
        "name": "Bánh canh Má Sáu",
        "address": "9 Nguyễn Thái Học, Phường 1, Tân An, Long An, Việt Nam",
        "phone": "0857878373",
        "image": "restaurant_images/banhcanh.jpg",
        "open_time": time(15, 0),
        "close_time": time(23, 0),
        "latitude": 10.537977401396544, 
        "longitude": 106.41583799965245,
        "rating": 4.9
    },
    {
        "name": "Hủ Tiếu Đường Hầm Tân An",
        "address": "GCQ9+FP9, Nguyễn Thái Bình, Phường 3, Tân An, Long An, Việt Nam",
        "phone": "",
        "image": "restaurant_images/hutiu.jpg",
        "open_time": time(10, 0),
        "close_time": time(22, 0),
        "latitude": 10.538694656556707, 
        "longitude": 106.4193946088176,
        "rating": 4.3
    },
    # ... (bạn tiếp tục bổ sung thêm các quán ăn khác theo mẫu này, với tọa độ thực tế từ Google Maps)
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
