# gil


Linguagem de programacao sem objetos, com palavras chaves simplificadas e tipagem fraca.

### Palavras Chaves:

* i: Equivalente ao tradicional "if", seguindo os padroes do C, mas sem a necessidade de parentesis, no entanto chaves sao sempre obrigatorias
* e: Equivalente ao "else", seguindo as mesmas regras do `i`
* f: Define uma funcao, segundo o padrao `f <nome da funcao>(<argumentos>) { <corpo da funcao> }`, devido a tipagem fraca, nao é necessario definir o tipo do retorno. Para retornar um valor na funcao, basta definir o mesmo em uma variável com o mesmo nome da funcao, caso esta variavel nao seja definida, o valor padrao de retorno da funcao sera `None`
* l: Definição de loop (`l <condicao de parada> { <corpo do loop> }`)
* in: Para entrada de dados, deve ser diretamente associado a uma variavel, tal como `j := in`
* out: Funcao para output de dados, recebe o dado em si como argumento, tal como `out 42`


### Instrucoes de Uso:

O projeto dispoe de um Pipfile, tal que para executa-lo basta utilizar o `pipenv` para instalar as dependencias (`pipenv install`) e depois rodar dentro da *shell* do pipenv (`pipenv shell`)
