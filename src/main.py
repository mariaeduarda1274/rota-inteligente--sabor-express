# main.py — versão final funcional (sem precisar de CSVs externos)

import folium
import statistics
from folium import Popup
import branca

# --- Dados simulados (exemplo para teste) ---
locais = [
    {'id': 'L1', 'lat': -23.5505, 'lon': -46.6333},  # São Paulo centro
    {'id': 'L2', 'lat': -23.5596, 'lon': -46.6588},  # Av. Paulista
]

entregas = [
    {'id': 'E1', 'lat': -23.5632, 'lon': -46.6544},
    {'id': 'E2', 'lat': -23.5650, 'lon': -46.6400},
    {'id': 'E3', 'lat': -23.5700, 'lon': -46.6500},
]

# --- Calcular centro do mapa ---
all_lats = [p['lat'] for p in locais + entregas]
all_lons = [p['lon'] for p in locais + entregas]
center = (statistics.mean(all_lats), statistics.mean(all_lons))

# --- Criar mapa ---
m = folium.Map(location=center, zoom_start=14, tiles='CartoDB positron')

# --- Locais (azul) ---
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

# --- Entregas (vermelho) ---
for p in entregas:
    folium.Marker(
        location=(p['lat'], p['lon']),
        icon=folium.Icon(color='red', icon='info-sign'),
        popup=Popup(f"Entrega ID: {p['id']}", parse_html=True)
    ).add_to(m)

# --- Rota simples (na ordem das entregas) ---
route_coords = [(p['lat'], p['lon']) for p in entregas]
if route_coords:
    folium.PolyLine(route_coords, color='#1976D2', weight=6, opacity=0.8).add_to(m)

# --- Legenda ---
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

# --- Salvar mapa ---
out_html = 'mapa_entregas.html'
m.save(out_html)
print(f"✅ Mapa gerado com sucesso: {out_html}")

#  ou também pode ser usado esse: 

# CÉLULA 1: LIMPEZA, DOWNLOAD E INSTALAÇÃO
!rm -rf rota-inteligente--sabor-express
!git clone https://github.com/mariaeduarda1274/rota-inteligente--sabor-express.git
%cd rota-inteligente--sabor-express
!pip install pandas folium branca selenium webdriver-manager

# CÉLULA 2: EXECUÇÃO DO SCRIPT!python src/main.py

# CÉLULA 3: BAIXAR O MAPA DE FORMA GARANTIDA!
cp /content/rota-inteligente--sabor-express/mapa_entregas.html /content/mapa_entregas.html
from google.colab import files
files.download("/content/mapa_entregas.html")































