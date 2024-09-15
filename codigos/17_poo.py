class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def logar_sistema(self):
        print(f"{self.nome} logado no sistema.")


class Aluno(Pessoa):
    def __init__(self, nome, data_matricula):
        super().__init__(nome)
        self.data_matricula = data_matricula

    def fazer_matricula_disciplina(self):
        print(f"Aluno {self.nome} fez matrícula em uma disciplina.")


class Professor(Pessoa):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def cadastrar_notas(self):
        print(f"Professor {self.nome} cadastrou notas.")


# Exemplo de uso:
aluno = Aluno(nome="João Bosco", data_matricula="2019-09-01")
aluno.logar_sistema()
aluno.fazer_matricula_disciplina()

professor = Professor(nome="Ana Maria", salario=15000)
professor.logar_sistema()
professor.cadastrar_notas()






