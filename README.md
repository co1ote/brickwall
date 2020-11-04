# Brickwall - Análise assintótica

Considerando a entrada uma matriz n x m. Onde é possível que n = m. 

O algoritmo possui 3 loops aninhados:
- Todos os cortes possiveis (n vezes);
- Cada fileira de tijolo (m vezes);
- Soma até chegar ou ultrapassar a posição do corte (n vezes);

> Portanto o algoritmo é O(n^3), polinomial.