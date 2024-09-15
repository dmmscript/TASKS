# Este arquivo depende do arquivo: 'montadora01.py'. Abra-o para ver seu conteúdo.
# O arquivo montadora01.py contém a classe 'Montadora'
# para acessar a classe 'Montadora' presente no arquivo 'montadora01.py' devemos fazer:

from montadora01 import Montadora

# Como dito, as classes são semelhantes a formas de bolo, Ao tirarmos um bolo de uma forma,
# este terá o formato desta forma. E esta forma sempre produzirá bolos com o mesmo formato.
# Assim são as classes, funcionam como moldes para a produção de bolos.

# Os bolos são os chamados 'Objetos'. Ao fazer um bolo, estamos de forma análoga criando
# um objeto. Ao invés de dizer "Criando um objeto" diga:  "Instanciando um objeto".

# Para instanciar um objeto é simples. Veja como se cria 2 objetos de nomes 'x' e 'y':

x = Montadora()
y = Montadora()

# Entendeu como se instancia um objeto? Basta atribuir a uma variavel, o nome da Classe. Lembre
# que a classe é uma forma de bolo.

# Neste caso, temos 2 "bolos" idênticos (x e y) os quais podem ser  estilizados (receber cobertura
# e recheios diferentes).

# Para estilizar um objeto, basta modificar seus atributos. Veja como:

# Alterando os atributos do objeto x:
x.cor = 'preta'
x.qtdLitros = 41
x.qtdPassageiros=5
x.tipoCombustivel='flex'
x.velocidade=0.0

# Alterando os atributos do objeto y:
y.cor = 'vermelha'
y.qtdLitros = 100
y.qtdPassageiros=6
y.tipoCombustivel='diesel'
y.velocidade=0.0

# Imprimindo os atributos de x e y:
print('Atributos de x:',x.cor,x.qtdLitros,x.qtdPassageiros,x.tipoCombustivel,x.velocidade)
print('Atributos de y:',y.cor,y.qtdLitros,y.qtdPassageiros,y.tipoCombustivel,y.velocidade)






