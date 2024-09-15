class Aluno:
    def __init__(self, nome, data_matricula):
        self.nome = nome
        self.data_matricula = data_matricula

    def logar_sistema(self):
        print(f"Aluno {self.nome} logado no sistema.")

    def fazer_matricula_disciplina(self):
        print(f"Aluno {self.nome} fez matrícula em uma disciplina.")


class Professor:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def logar_sistema(self):
        print(f"Professor {self.nome} logado no sistema.")

    def cadastrar_notas(self):
        print(f"Professor {self.nome} cadastrou notas.")


# Exemplo de uso:
aluno = Aluno(nome="João", data_matricula="2024-09-01")
aluno.logar_sistema()
aluno.fazer_matricula_disciplina()

professor = Professor(nome="Carlos", salario=5000)
professor.logar_sistema()
professor.cadastrar_notas()



