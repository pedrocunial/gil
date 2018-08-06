# gil


Linguagem de programacao sem objetos e com palavras chaves simplificadas e tipagem fraca.

### Palavras chaves:

* i: Equivalente ao tradicional "if", seguindo os padroes do C, mas sem a necessidade de parentesis, no entanto chaves sao sempre obrigatorias;
* ei: Equivalente ao "else if", mantem os padroes acima;
* f: Define uma funcao, segundo o padrao "f <nome da funcao>(<argumentos>) { <corpo da funcao> }", devido a tipagem fraca, nao é necessario definir o tipo do retorno, no entanto, uma funcao definida com "f" *sempre* devera retornar algo
* m: Funcao sem retorno, segue a mesma assinatura do "f"
* l: Definicao de loop, segue a assinatura "l <cond inicial>; <cond final>; <passo> { <corpo do loop> }". Adicionalmente, loops infinitos podem ser declarados sem especificar nenhum dos argumentos ("l { <corpo do loop> }") e argumentos podem ser "ignorados" ("l ; k < 2; k++", onde "k" seria uma variavel previamente definida)
* in: Para entrada de dados, deve ser diretamente associado a uma variavel, tal como "j = in"
* out: Funcao para output de dados, recebe o dado em si como argumento, tal como "out('Olá Mundo!')"


### Características adicionais:

* Nao distincao entre *chars* e *strings*
* Possibilidade de uso de ' ou " para a definicao de *strings*
* Nao existem numeros de ponto-flutuante ("é só dividir por 10 no final rsrs")
* Sem ponto e vírgula!
