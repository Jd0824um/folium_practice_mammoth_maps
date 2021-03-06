import folium
import csv

mammoth_colors = {'Mammuthus columbi': 'green',
                  'Mammuthus primigenius': 'blue',
                  'Mammuthus hayi': 'purple',
                  'Mammuthus exilis': 'red',
                  'Mammuthus': 'orange'}

mammoth_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')


with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()

    for line in reader:
        if line:
            lat = line[3]
            lon = line[4]
            marker_txt = '%s found in %s, %s. %s.' % (line[0], line[6], line[5], line[7])
            if line[1]:
                marker_txt += ' %s %s ' % (line[1], line[2])

            color = mammoth_colors[line[0]]

            marker = folium.Marker([lat, lon], popup=marker_txt, icon=folium.Icon(color=color))
            marker.add_to(mammoth_map)

mammoth_map.save('mammoth_map.html')