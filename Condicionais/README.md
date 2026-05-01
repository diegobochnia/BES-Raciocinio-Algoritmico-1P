### Lista de Exercícios: Condicionais

1. **Votação**: Crie um programa que pergunte a idade do usuário e verifique se ele tem idade para votar.
   - O voto é permitido para quem tem 16 anos ou mais.
   - Se a idade for maior ou igual a 16, exiba: `"Você já pode votar!"`.
   - Caso contrário, exiba: `"Você ainda não tem idade para votar."`.

2. **Positivo, Negativo ou Zero**: Crie um programa que peça um número inteiro ao usuário.
   - Se o número for maior que zero, exiba: `"O número X é Positivo."`.
   - Se for menor que zero, exiba: `"O número X é negativo."`.
   - Caso contrário, exiba: `"O número é Zero."`.

3. **Desconto do Cliente**: Peça ao usuário o valor total de uma compra (use `float()`).
   - Se o valor for maior que `R$ 100,00`, aplique um desconto de 10% e mostre o valor final a pagar.
   - Se for menor ou igual a `R$ 100,00`, exiba o valor normal e a mensagem: `"Nas compras acima de R$ 100, você ganha 10% de desconto!"`.

4. **Sistema de Notas**: Peça ao usuário uma nota (use `float()`) e classifique conforme os critérios abaixo:
   - Maior ou igual a `9.0`: `"Parabéns!! Você foi aprovado!"`.
   - Entre `7.0` e `8.9`: `"Aprovado."`.
   - Entre `4.0` e `6.9`: `"Em Recuperação"`.
   - Menor que `4.0`: `"Reprovado"`.

5. **Par ou Ímpar**: Peça ao usuário um número inteiro. Use o operador de resto `%` para verificar se o número é par ou ímpar e exiba a mensagem correspondente.

6. **Comparando Dois Números**: Peça dois números ao usuário. O programa deve informar qual deles é o maior ou, caso sejam iguais, informar isso também.

7. **Verificação de Login**: Crie uma variável `usuario_correto` com o valor `"admin"`. Peça ao usuário que digite um nome de usuário e:
   - Se for igual ao armazenado, exiba: `"Acesso concedido"`.
   - Caso contrário, exiba: `"Usuário desconhecido"`.

8. **Calculadora de IMC Simples**: Peça o peso e a altura do usuário. Calcule o IMC com a fórmula `peso / altura²` e:
   - Se o IMC for maior que `25`, exiba: `"Acima do peso ideal"`.
   - Caso contrário, exiba: `"Peso dentro da normalidade"`.

9. **Classificação de Triângulos**: Peça os três lados de um triângulo e classifique:
   - Todos os lados iguais: `"Equilátero"`.
   - Apenas dois lados iguais: `"Isósceles"`.
   - Todos os lados diferentes: `"Escaleno"`.

10. **Múltiplo de 5**: Peça um número ao usuário e informe se ele é um múltiplo de 5.

11. **Categorias de Atleta**: Solicite a idade de um nadador e classifique-o conforme a tabela:
    - 5 a 7 anos: `Infantil A`.
    - 8 a 10 anos: `Infantil B`.
    - 11 a 13 anos: `Juvenil A`.
    - 14 a 17 anos: `Juvenil B`.
    - 18 anos ou mais: `Adulto`.

12. **Calculadora de Viagem**: Pergunte a distância que um passageiro deseja percorrer em km e calcule o preço da passagem:
    - Até 200 km: `R$ 0,50` por km.
    - Acima de 200 km: `R$ 0,45` por km.

13. **Ano Bissexto**: Peça ao usuário um ano (ex.: `2024`) e informe se ele é bissexto (divisível por 4).

14. **Aumento Salarial**: Peça o salário de um funcionário e calcule o reajuste:
    - Salário superior a `R$ 1.621,00`: aumento de `10%`.
    - Salário inferior ou igual: aumento de `15%`.

15. **Simulador de Radar**: Pergunte ao usuário a velocidade de um carro. Se ultrapassar `80 km/h`, exiba uma mensagem informando que o usuário foi multado. O valor da multa é de `R$ 7,00` por cada km acima do limite.

16. **Conversor de Temperatura**: Peça ao usuário uma temperatura em Celsius e pergunte se deseja converter para Fahrenheit (`F`) ou Kelvin (`K`). Exiba o resultado conforme a opção escolhida.
    - Celsius para Fahrenheit: `(°C × 9/5) + 32`
    - Celsius para Kelvin: `°C + 273,15`

17. **Loja de Tintas**: Peça o tamanho em m² da área a ser pintada. Considere que 1 litro de tinta cobre 3 m² e que a tinta é vendida em latas de 18 litros a `R$ 80,00`. Informe ao usuário se ele precisa de apenas uma lata ou de mais de uma.

18. **Aprovação de Empréstimo**: Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele pretende pagar. O empréstimo será aprovado somente se a prestação mensal não exceder 30% do salário; caso contrário, deverá ser negado.