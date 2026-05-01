### Lista de Exercícios: Matrizes

1. **Soma Total**: Crie uma matriz 3×3 de números inteiros e exiba a soma de todos os elementos.

2. **Matriz Identidade**: Peça ao usuário um valor `n` e gere uma Matriz Identidade de ordem `n`.

3. **Busca Simples**: Dada uma matriz 4×4, peça um número ao usuário e diga se esse número está ou não na matriz.

4. **Troca de Linhas**: Crie uma matriz 2×2 e troque os valores da primeira linha com os da segunda linha.

5. **Multiplicação por Escalar**: Leia uma matriz 3×3 e um número real. Exiba a matriz resultante da multiplicação de cada elemento por esse número.

6. **Contagem de Pares**: Dada uma matriz 3×4, conte quantos números pares ela possui.

7. **Maior Elemento**: Crie uma matriz preenchida com números aleatórios e encontre qual é o maior valor presente nela.

8. **Média por Linha**: Crie uma matriz 3×3 e exiba a média aritmética dos valores de cada linha separadamente.

9. **Soma da Diagonal Principal**: Calcule a soma de todos os elementos que compõem a diagonal principal de uma matriz 4×4.

10. **Matriz Transposta**: Escreva um programa que receba uma matriz M×N e gere a sua transposta (N×M).

11. **Soma de Colunas**: Crie uma matriz 3×3 e gere uma lista de 3 elementos onde cada elemento é a soma de uma coluna da matriz.

12. **Verificação de Simetria**: Verifique se uma matriz quadrada é simétrica (onde a matriz é igual à sua transposta).

13. **Diagonal Secundária**: Exiba apenas os elementos da diagonal secundária de uma matriz 5×5.

14. **Multiplicação de Matrizes**: Implemente a multiplicação de duas matrizes. Lembre-se: para multiplicar A por B, o número de colunas de A deve ser igual ao número de linhas de B.

15. **Rotação 90°**: Crie um algoritmo que rotaciona uma matriz quadrada n×n em 90 graus no sentido horário, sem usar bibliotecas como NumPy.

---

### Exercícios de Fixação: Matrizes com NumPy

> ⚠️ **Observação:** use `import numpy as np` no início de cada script.

1. **Chuva Total por Região**: Você faz parte de uma equipe que monitora a quantidade de chuva em uma cidade ao longo de alguns dias. Os dados são organizados em matrizes onde cada linha representa um dia e cada coluna representa uma região da cidade.

   Crie um algoritmo em Python utilizando NumPy que:
   - Cria duas matrizes 3×3: `manha` e `tarde`.
   - Some as duas matrizes para obter a matriz `total`, representando a quantidade total de chuva por dia e por região.
   - Exiba a matriz da manhã, a matriz da tarde e a matriz total.

2. **Controle de Estoque**: Você trabalha no controle de estoque de uma loja. Uma matriz representa a quantidade de produtos antes das vendas e outra representa a quantidade vendida.

   Crie um algoritmo em Python com NumPy que:
   - Crie duas matrizes 3×3: `estoque_inicial` e `vendidos`.
   - Calcule a matriz `estoque_final` conforme a fórmula:
     ```
     estoque_final = estoque_inicial - vendidos
     ```
   - Exiba todas as matrizes.

3. **Sistema de Lanchonete**: Você está ajudando a montar o sistema de uma lanchonete. Uma matriz representa a quantidade de ingredientes por lanche e outra representa a quantidade de lanches pedidos.

   Crie um algoritmo com NumPy que:
   - Crie uma matriz `ingredientes` (ex.: 2×3).
   - Crie uma matriz `pedidos` (ex.: 3×2).
   - Realize a multiplicação das matrizes e exiba o resultado.

4. **Reajuste Salarial**: Você trabalha no RH de uma empresa. A matriz representa os salários de funcionários em diferentes setores. A empresa decidiu aplicar um aumento de 10% para todos.

   Crie um algoritmo com NumPy que:
   - Crie uma matriz 3×3 chamada `salarios`.
   - Multiplique toda a matriz por `1.10`.
   - Exiba a matriz original e a matriz reajustada.

5. **Zerando a Matriz**: Você está reiniciando um sistema que armazena dados temporários e precisa zerar a matriz.

   Crie um algoritmo com NumPy que:
   - Crie uma matriz 3×3 com valores quaisquer.
   - Transforme todos os valores da matriz em `0`.
   - Exiba a matriz final.

6. **Ativando Sensores**: Um sistema foi iniciado e todos os sensores precisam começar ativos. Na matriz, `1` significa ativo.

   Crie um algoritmo com NumPy que:
   - Crie uma matriz 4×4 com valores quaisquer.
   - Altere todos os valores da matriz para `1`.
   - Exiba a matriz final.

7. **Corrigindo Valores**: Você encontrou um erro em um sistema: valores específicos da matriz estão incorretos.

   Crie um algoritmo com NumPy que:
   - Crie uma matriz 5×5 com valores inteiros.
   - Substitua o valor das posições: linha 1 coluna 2, e linha 3 coluna 5.
   - Defina novos valores para essas posições.
   - Exiba a matriz antes e depois da alteração.