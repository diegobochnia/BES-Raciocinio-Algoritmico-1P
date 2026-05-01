# Lista de Exercícios: Funções
###OBS: Alguns dos seguintes exercícios não estão no repositório pois não foram resolvidos em um arquivo .py

1. **Soma**: Crie uma função `somar(a, b)` que retorne a soma de dois números.

2. **Multiplicação**: Crie uma função `multiplicar(a, b)` que retorne o resultado da multiplicação.

3. **Saudação Simples**: Escreva uma função `mensagem(nome)` que imprima: `Olá, <nome>!`.

4. **Maior Valor**: Crie uma função `maior(a, b)` que retorne o maior entre dois números.

5. **Divisão Inteira**: Crie uma função `dividir(a, b)` que retorne o quociente e o resto da divisão.

6. **Verificação de Paridade**: Crie uma função `par_ou_impar(n)` que retorne `True` se for par e `False` caso contrário.

7. **Análise de Retorno**: O que será exibido no código abaixo?
   ```python
   def teste():
       print('Olá')

   resultado = teste()
   print(resultado)
   ```

8. **Apresentação de Dados**: Crie uma função `apresentar(nome, idade, cidade)` que imprima os dados formatados.

9. **Argumentos Posicionais e Nomeados**: Chame a função `apresentar` usando argumentos posicionais e nomeados.

10. **Ordem de Argumentos**: O que acontece ao chamar `apresentar('Ana', 'Curitiba', 20)`?

11. **Valor Padrão**: Crie uma função `saudacao(nome, periodo='dia')`.

12. **Sobrescrita de Padrão**: Modifique a função `saudacao` para aceitar tanto o valor padrão quanto um valor informado.

13. **Erro de Sintaxe**: Explique o erro no código abaixo:
    ```python
    def exemplo(a=1, b):
        ...
    ```

14. **Soma Variádica**: Crie uma função `somar_todos(*numeros)` que some uma quantidade arbitrária de valores.

15. **Exibição de Dicionário**: Crie uma função `mostrar_dados(**dados)` que exiba pares chave-valor.

16. **`*args` vs `**kwargs`**: Explique a diferença entre `*args` e `**kwargs`.

17. **Escopo de Variáveis**: O que será exibido no código abaixo?
    ```python
    x = 10

    def teste():
        x = 5
        print(x)

    teste()
    print(x)
    ```

18. **Variável Global**: Corrija o código abaixo para que funcione corretamente:
    ```python
    contador = 0

    def incrementar():
        contador += 1
    ```

19. **Funções como Objetos**: Crie uma função `triplo(x)` e atribua-a a uma variável.

20. **Funções de Alta Ordem**: Crie uma função `executar(funcao, valor)` que receba outra função como argumento e a execute com o valor fornecido.

21. **Lambda**: Reescreva `quadrado(x)` usando uma expressão `lambda`.

22. **`map`**: Use `map` para dobrar todos os elementos de `[1, 2, 3, 4, 5]`.

23. **`filter`**: Use `filter` para retornar apenas os números pares de uma lista.

24. **Fatorial Recursivo**: Crie uma função `fatorial(n)` usando recursão.

25. **Contagem Regressiva**: Crie uma função recursiva que faça a contagem de `n` até `0`.

26. **Erro de Recursão**: Explique o problema no código abaixo:
    ```python
    def erro(n):
        return n * erro(n - 1)
    ```

27. **Docstring**: Crie uma função `media(lista)` com uma docstring explicativa.

28. **`help()`**: Use `help()` para exibir a documentação da função criada no exercício anterior.

29. **Calculadora**: Crie uma função `calculadora(a, b, operacao)` que receba uma operação como argumento e execute-a sobre `a` e `b`.

30. **Processamento Genérico**: Crie uma função `processar_dados(*args, **kwargs)` que receba e exiba qualquer combinação de argumentos.