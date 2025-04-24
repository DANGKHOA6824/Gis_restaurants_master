// Khởi tạo bản đồ
var map = L.map('map').setView([10.5354, 106.4145], 14);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Marker vị trí hiện tại: pulse xanh dương
var userIcon = L.icon.pulse({iconSize:[18,18], color:'#2196f3', fillColor:'#2196f3', heartbeat:1.1});

// Marker đỏ cho các quán ăn
var restaurantIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var userMarker = null;
var userLatLng = null;
var routingControl = null;

// Nút "Đến vị trí của tôi"
var lc = L.control.locate({
    position: 'topleft',
    strings: {
        title: "Đến vị trí của tôi"
    },
    drawCircle: true,
    keepCurrentZoomLevel: true,
    showPopup: false,
    locateOptions: {
        enableHighAccuracy: true
    }
}).addTo(map);

// Khi xác định được vị trí, marker pulse xanh, tooltip nhỏ
map.on('locationfound', function(e) {
    if (userMarker) map.removeLayer(userMarker);
    userMarker = L.marker(e.latlng, {icon: userIcon}).addTo(map)
        .bindTooltip("Bạn đang ở đây", {permanent: true, direction: 'top', offset: [0, -10], className: 'my-location-tooltip'});
    userLatLng = e.latlng;
    showRestaurants();
});

map.on('locationerror', function(e) {
    alert("Không lấy được vị trí của bạn: " + e.message);
    showRestaurants();
});

// Hiển thị các quán ăn và popup
function showRestaurants() {
    fetch("/api/restaurants/")
        .then(response => response.json())
        .then(data => {
            data.forEach(function(item) {
                var distance = "";
                if (userLatLng) {
                    var d = map.distance([item.latitude, item.longitude], [userLatLng.lat, userLatLng.lng]);
                    if (d > 1000) {
                        distance = (d/1000).toFixed(2) + " km";
                    } else {
                        distance = Math.round(d) + " m";
                    }
                }
                var stars = "★".repeat(Math.round(item.rating)) + "☆".repeat(5 - Math.round(item.rating));
                var popupContent =
                    `<img src="${item.image}" class="popup-img" alt="${item.name}"/>
                    <div class="popup-title">${item.name}</div>
                    <div class="popup-rating">${stars} <span style="color:#555;font-size:0.9em;">(${item.rating}/5)</span></div>
                    <div class="popup-info"><b>Địa chỉ:</b> ${item.address}</div>
                    <div class="popup-info"><b>Điện thoại:</b> ${item.phone}</div>
                    <div class="popup-info"><b>Giờ mở cửa:</b> ${item.open_time} - ${item.close_time}</div>
                    ${distance ? `<div class="popup-distance">📍 Khoảng cách: ${distance}</div>` : ""}
                    <div class="popup-actions">
                        <button class="btn-route" onclick="showRoute(${item.latitude},${item.longitude},'${item.name.replace(/'/g,"\\'")}')">
                            🧭 Chỉ đường
                        </button>
                        <a href="/restaurant/${item.id}/" class="btn-detail">
                            📋 Chi tiết
                        </a>
                    </div>`;
                L.marker([item.latitude, item.longitude], {icon: restaurantIcon}).addTo(map)
                    .bindPopup(popupContent, {className: 'custom-popup'});
            });
        });
}

// Vẽ đường đi nhanh nhất bằng OSRM mặc định của Leaflet Routing Machine
function showRoute(destLat, destLng, destName) {
    if (!userLatLng) {
        alert("Không xác định được vị trí của bạn!");
        return;
    }
    if (routingControl) {
        map.removeControl(routingControl);
    }
    routingControl = L.Routing.control({
        waypoints: [
            L.latLng(userLatLng.lat, userLatLng.lng),
            L.latLng(destLat, destLng)
        ],
        fitSelectedRoutes: false, // Không tự động zoom lại khi chỉ đường
        show: false,
        addWaypoints: false,
        draggableWaypoints: false,
        routeWhileDragging: false
    }).addTo(map);
}

// Tự động lấy vị trí khi load trang
map.locate({setView: true, maxZoom: 15});
