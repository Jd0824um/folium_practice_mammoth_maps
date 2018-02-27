import folium

map_mn = folium.Map(location=[40, -120], zoom_start=3)

map_mn.save('map_us.html')