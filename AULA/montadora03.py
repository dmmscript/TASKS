
# Encapsular um atributo significa restringir o seu acesso somente por meio de outros métodos.
# Diferente de outras linguagens de POO, Python não encapsula seus atributos usando os modificadores
# de acesso (private, public, protected).
# Apenas para nos situarmos:

#    public: fornece livre acesso
#    private: limita o acesso apenas por métodos
#    protected: apenas classes filhas podem acessar (veremos isso em Herança)

# Python tem apenas o conceito de public e private!
# Para definir um atributo como public, basta declará-lo normalmente (como já fizemos)
# Para definir um atributo como private, basta colocar um duplo underscore (__) antes do atributo.
# De fato, Python nao ira bloquear o acesso aos atributos, pois eles poderao ser acessados por 
# _NomeDaClasse__nome_do_atributo. Ou seja, cabe ao programador usar o bom senso e evitar o acesso
# direto a pois isto pode criar dependências indesejadas e tornar o código mais difícil de manter.


class Montadora:
    def __init__(self, cor, velocidade, qtdPassageiros, tipoCombustivel, qtdLitros):
        self.__cor=cor
        self.__velocidade=velocidade
        self.__qtdPassageiros=qtdPassageiros
        self.__tipoCombustivel=tipoCombustivel
        self.__qtdLitros=qtdLitros

# Vamos agora para o arquivo 'main03.py' instanciar um objeto e tentar acessa-lo.
