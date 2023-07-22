# Aggregates

Uma entidade agregada é uma coleção de objetos relacionados que são tratados 
como uma única unidade coesa dentro do domínio do problema. Ela é responsável 
por garantir a consistência e as invariantes de negócio para o conjunto de 
objetos que a compõem. Uma das principais características de uma entidade 
agregada é que ela possui uma raiz de agregado (aggregate root), que é a 
única entidade que pode ser referenciada externamente e é responsável por 
manter o acesso e a consistência dos demais objetos dentro da agregação. 

Por exemplo, considere um sistema bancário, onde um cliente tem várias contas 
bancárias. Nesse caso, o cliente seria a raiz de agregado e suas contas 
bancárias seriam objetos dentro dessa agregação. O cliente seria a única 
entidade acessível de fora da agregação, e qualquer alteração nas contas do 
cliente seria feita através dele para manter a integridade do conjunto. 

Em resumo, objetos de valor são componentes imutáveis e identificados apenas 
por seus atributos, enquanto entidades agregadas são coleções de objetos 
relacionados, onde um deles atua como raiz e é a única entidade acessível 
externamente. Esses conceitos ajudam a simplificar a modelagem do domínio e a 
manter a consistência e a integridade dos dados dentro do sistema.