## Execução do projeto ## 
Google Colab 
1. Acesse o notebook no Google Colab 
2. Execute as células em ordem. 
> O projeto foi desenvolvido e testado integralmente no **Google Colab**.
# Biblioteca ultilizada: PANDAS
# Algoritmos ultilizados: 
- K- Means: agrupa os pontos de entrega para aprimorar o resultado final 
- A\*: Calcula a rota mais curta entre pontos 
- BFS: Busca em Largura 
- Dfs: Busca em Profundidade 

## Dados utilizados ##
Data/ 
* deliveries.csv
*map_edges.csv
* pontos.csv 

## Documentação e resultados 
Docs/ 
* mapa_entregas.png 

## Código - fonte principal 
* main.py

## Projeto Rota Inteligente - Sabor Express ##

Este projeto gera um mapa HTML interativo (`mapa_entregas.html`) com os locais de entregas, pontos de interesse e a rota de percurso otimizado.

Para executar o projeto no **Google Colab**, siga os passos abaixo em três células distintas e sequenciais:

---

# CÉLULA 1: LIMPEZA, DOWNLOAD E INSTALAÇÃO
# Garante que o Colab baixe a versão FINAL e CORRIGIDA do main.py
!rm -rf rota-inteligente--sabor-express
!git clone https://github.com/mariaeduarda1274/rota-inteligente--sabor-express.git
%cd rota-inteligente--sabor-express 
!pip install pandas folium branca selenium webdriver-manager

# CÉLULA 2: EXECUÇÃO DO SCRIPT
!python src/main.py

# CÉLULA 3: BAIXAR O MAPA DE FORMA GARANTIDA
!cp /content/rota-inteligente--sabor-express/mapa_entregas.html /content/mapa_entregas.html

from google.colab import files
files.download("/content/mapa_entregas.html")
