# Value Objects

Um objeto de valor é um conceito que representa uma característica ou 
atributo importante dentro do domínio do problema. Eles são chamados de 
"objetos de valor" porque seu valor é definido pelo conjunto de atributos que 
eles contêm e não têm identidade própria. Em outras palavras, dois objetos de 
valor são considerados iguais se seus atributos forem iguais. Eles são 
imutáveis, ou seja, uma vez criados, seus atributos não podem ser alterados. 

Um exemplo de objeto de valor poderia ser uma data (com dia, mês e ano), uma 
coordenada geográfica (latitude e longitude) ou um endereço (com rua, número, 
cidade, etc.). Nesses casos, a identidade do objeto não importa tanto quanto 
os valores dos atributos que ele contém. 

Em resumo, objetos de valor são componentes imutáveis e identificados apenas 
por seus atributos, enquanto entidades agregadas são coleções de objetos 
relacionados, onde um deles atua como raiz e é a única entidade acessível 
externamente. Esses conceitos ajudam a simplificar a modelagem do domínio e a 
manter a consistência e a integridade dos dados dentro do sistema.