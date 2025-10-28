## 📌 Rota Inteligente: Otimização de Entregas (Sabor Express)


## 🛑1. Descrição do problema e objetivos 
** Problema:** A Sabor Express faz entregas com rotas montadas manualmente. Em horários de picos causa atrasos, mais gasto de combustível e clientes insatisfeitos. 

** Desafio:** Criar uma solução que sugira rotas melhores automaticamente e agrupe entregas próximas para reduzir tempo e custo das entregas.

** Objetivos:** (1) representar a cidade como um grafo; (2) calcular rotas curtas entre pontos; (3) agrupar entregas próximas em zonas; (4) documentar e apresentar os resultados 

## 🎯 2. Abordagem adotada 
1. ** Modelagem:** transformei a cidade num grafo - cada local é um ponto do mapa  (com coordenadas) e cada rua é uma aresta com peso( distância).
2. ** Roteamento:** para achar o menor caminho entre dois pontos usei A*, e serve também para varias coisas, como mostra acidentes no caminho, pedágios.. um exemplo é  o GPS do Google Maps.
3. ** Agrupamento:** quando há muitos pedidos, uso K-Means para agrupar entregas próximas em zonas, assim um entregador cuida de um grupo por vez
4. ** Visualização:** gerei um gráfico do grafo mostrando os nós, arestas, entregas e uma rota de exemplo para facilitar a apresentação.

 ## ⚙️3. Algoritmos usados
 - **A\*** - busca informada para obter rotas curtas rápido.
 - ** BFS/ DFS** - usados para testar conectividade e percorrer o grafo
 - ** K- Means** - agrupa entregas próximas para formar zonas eficientes, isso faz até com que economize combustível ja que vai ser mais em grupos de zonas.

## 🗺️ 4. Diagrama do grafo/ modelo 
Inclui a imagem:
<img width="1363" height="614" alt="image" src="https://github.com/user-attachments/assets/28806afa-2a8a-465b-ac65-d83c57d0d978" />
Ela mostra: 
- pontos azuis= nós do mapa( locais);
- linhas cinza= arestas(ruas); 
- pontos vermelhos = entregas;
- linhas em destaque = rota calculada(A*)
Link que caso não queira a imagem, até para mexer com mouse para apliar o mapa.
https://mariaeduarda1274.github.io/rota-inteligente--sabor-express/

## 📊 5. Análise dos resultados
Testes feitos com dados inexistentes(exemplo):
- Nós: 3 | Entregas: 3
- Rota sequencial exemplo: ~ 100.000 unidades de distância.
- K Means formou 3 agrupamentos, facilitando a divisão por entregador

## 6. Eficiência da solução 
- **A\*** costuma ser um pouco mais complexo visualmente, mas na prática é muito mais rápido
- **K-Means** depende do número de entregas para estipular seu custo
- Para um pequeno negócio( mapa pequeno e poucas entregas) o tempo de execução é baixo

## 7. Limitações 
- Dados usados foram sintéticos
- Não foram consideradas janelas de horário, capacidade dos entregadores ou ruas com sentido único.
- Visualização estática, e um pouco com o web

## 🔨8. Sugestões de melhoria 
- Integrar dados reais e tráfego em tempo real
- Implementar interface de web mais detalhada
- Teqstar em dados reais da Sabor Express e ajustar parâmetros segundo números de entregadores.

## 💡9. Conclusão: 
- A solução mostrou que, mesmo com técnicas clássicas, é possivel automatizar e melhorar rotas de entrega, reduzindo deslocamento e organizando melhor as tarefas dos entregadores. Com dados reais e melhorias listadas, a ferramenta pode se tornar prática para uso diário, e com isso tendo muitas melhorias, economizando combustível, otimizando tempo.. 




















