# main.py ( feito no Google Colab) - código principal da Rota Inteligente 
print("Sistema de rotas inteligentes funcionando!")

## Rodar o projeto no Google Colab
Você pode abrir e executar este projeto diretamente no Google Colab:

#[🟢 Abrir no Colab](https://colab.research.google.com/drive/1TtVJR9XAC6IMIcnjiECM6q1OVqcpwTeb?usp=sharing)

!pip install folium branca
!pip install selenium webdriver-manager
from google.colab import files
uploaded = files.upload()
import pandas as pd
df = pd.read_csv("data/pontos.csv")
print(df)
from google.colab import files
uploaded = files.upload()
import pandas as pd
df = pd.read_csv("data/deliveries.csv")
print(df)

# gera_mapa_entregas.py
import folium
import csv
import statistics
from folium import Popup
import branca

# --- carregar dados ---
def load_csv_points(path, lat_col='lat', lon_col='lon'):
    pts = []
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            pts.append({
                'id': row.get('id'),
                'lat': float(row[lat_col]),
                'lon': float(row[lon_col]),
                'raw': row
            })
    return pts

locais = load_csv_points('pontos.csv', lat_col='lat', lon_col='lon')
entregas = load_csv_points('deliveries.csv', lat_col='lat', lon_col='lon')

# --- centro do mapa ---
all_lats = [p['lat'] for p in locais + entregas]
all_lons = [p['lon'] for p in locais + entregas]
center = (statistics.mean(all_lats), statistics.mean(all_lons))

# --- criar mapa folium ---
m = folium.Map(location=center, zoom_start=14, tiles='CartoDB positron')  # estilo limpo e moderno

# --- adicionar marcadores (locais azul) ---
for p in locais:
    folium.CircleMarker(
        location=(p['lat'], p['lon']),
        radius=6,
        color='#1f77b4',
        fill=True,
        fill_color='#1f77b4',
        fill_opacity=0.9,
        popup=Popup(f"Local ID: {p['id']}", parse_html=True)
    ).add_to(m)

# --- marcadores de entregas (vermelho) ---
for p in entregas:
    folium.Marker(
        location=(p['lat'], p['lon']),
        icon=folium.Icon(color='red', icon='info-sign'),
        popup=Popup(f"Entrega ID: {p['id']}", parse_html=True)
    ).add_to(m)

# --- rota otimizada (exemplo) ---
# Aqui você coloca a lista de coordenadas na ordem do percurso otimizado (lat, lon).
# No exemplo abaixo eu simplifico criando uma rota passando por todas as entregas na ordem do arquivo.
route_coords = [(p['lat'], p['lon']) for p in entregas]
# Se quiser incluir um ponto de partida, adicione-o antes: route_coords.insert(0, (start_lat,start_lon))

if route_coords:
    folium.PolyLine(route_coords, color='#1976D2', weight=6, opacity=0.8).add_to(m)

# --- legenda custom (usando branca) ---
legend_html = """
<div style="
position: fixed;
bottom: 30px; left: 30px; width: 150px; height: 110px;
background-color: white; border:2px solid grey; z-index:9999; font-size:14px;
box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
">
&nbsp;<b>Legenda</b><br>
&nbsp;<i style="color:#1f77b4;">●</i>&nbsp; Locais<br>
&nbsp;<i style="color:red;">●</i>&nbsp; Entregas<br>
&nbsp;<i style="color:#1976D2;">──</i>&nbsp; Rota ótima
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# --- salvar HTML ---
out_html = 'mapa_entregas.html'
m.save(out_html)
print(f"Mapa salvo em: {out_html}")

import folium

# Criar o mapa
mapa = folium.Map(location=[-23.55, -46.63], zoom_start=12)

# Adicionar marcador de exemplo
folium.Marker([-23.55, -46.63], popup="Exemplo").add_to(mapa)

# Salvar como HTML
mapa.save("mapa_entregas.html")

from google.colab import files
files.download("mapa_entregas.html")
