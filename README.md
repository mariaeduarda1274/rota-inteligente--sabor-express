# Rota Inteligente: Otimização de Entregas (Sabor Express)

## 1. Descrição do problema e objetivos 
** Problema:** A Sabor Express faz entregas com rotas montadas manualmente. Em horários de picos causa atrasos, mais gasto de combustível e clientes insatisfeitos. 
** Desafio:** Criar uma solução que sugira rotas melhores automaticamente e agrupe entregas próximas para reduzir tempo e custo das entregas.
** Objetivos:** (1) representar a cidade como um grafo; (2) calcular rotas curtas entre pontos; (3) agrupar entregas próximas em zonas; (4) documentar e apresentar os resultados 

## 2. Abordagem adotada 
1. ** Modelagem:** transformei a cidade num grafo - cada local é um ponto do mapa  (com coordenadas) e cada rua é uma aresta com peso( distância).
2. ** Roteamento:** para achar o menor caminho entre dois pontos usei A*, e serve também para varias coisas, como mostra acidentes no caminho, pedágios.. um exemplo é  o GPS do Google Maps.
3. ** Agrupamento:** quando há muitos pedidos, uso K-Means para agrupar entregas próximas em zonas, assim um entregador cuida de um grupo por vez
4. ** Visualização:** gerei um gráfico do grafo mostrando os nós, arestas, entregas e uma rota de exemplo para facilitar a apresentação.

 ## 3. Algoritmos usados
 - **A\*** - busca informada para obter rotas curtas rápido.
 - ** BFS/ DFS** - usados para testar conectividade e percorrer o grafo
 - ** K- Means** - agrupa entregas próximas para formar zonas eficientes, isso faz até com que economize combustível ja que vai ser mais em grupos de zonas.

## 4. Diagrama do grafo/ modelo 
# inclui a imagem: no repositório 
<img width="1363" height="614" alt="image" src="https://github.com/user-attachments/assets/28806afa-2a8a-465b-ac65-d83c57d0d978" />
# link que caso não queira ja a imagem tem o link. 
https://mariaeduarda1274.github.io/rota-inteligente--sabor-express/


















