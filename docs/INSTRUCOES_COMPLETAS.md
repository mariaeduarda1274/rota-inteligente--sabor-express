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

## Célula 1: Setup e Instalação (Clonar e Instalar)

Este bloco clona o repositório **correto**, navega para a pasta do projeto e instala todas as bibliotecas necessárias.

```python
# CÉLULA 1#: LIMPEZA, DOWNLOAD E INSTALAÇÃO
# Garante que a versão final do código seja baixada
!rm -rf rota-inteligente--sabor-express 
!git clone [https://github.com/mariaeduarda1274/rota-inteligente--sabor-express.git](https://github.com/mariaeduarda1274/rota-inteligente--sabor-express.git)
%cd rota-inteligente--sabor-express 

# INSTALAR DEPENDÊNCIAS
!pip install pandas folium branca selenium webdriver-manager

Python
# CÉLULA 2: EXECUÇÃO DO SCRIPT
!python src/main.py

# Célula 3 #: Download do Resultado Final

# Move o mapa da pasta do projeto para a raiz do Colab para o download funcionar
!cp /content/rota-inteligente--sabor-express/mapa_entregas.html /content/mapa_entregas.html

from google.colab import files
files.download("/content/mapa_entregas.html")
