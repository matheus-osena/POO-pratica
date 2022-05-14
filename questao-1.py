"""1. **Escreva um programa java para ler dados de várias pessoas (nome, idade e cpf) e guardar num vetor. 
O programa deverá ler os dados de 3 pessoas, depois exibi-los.**"""

class Pessoa():
    lista_cpf =[]
    
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cpf = None

    def receber_nome(self):
        validador = 1
        while validador == 1:
            try:
                self.nome = input("Digite o seu nome: \n")
                validador = 0
            except(Exception):
                print("Nome inválido.\n")

    
    def receber_idade(self):
        validador = 1
        while validador == 1:
            try:
                self.idade = int(input("Digite a sua idade: \n"))
                validador = 0
            except(Exception):
                print("Esse campo deve conter somente números. Digite novamente: \n")
    
    def receber_cpf(self):
        validador = 1
        while validador == 1:
            try:
                self.cpf = input("Digite o seu cpf (Somente números): \n").replace(" ", "")
                if self.cpf.isnumeric() == False or len(self.cpf) != 11:
                    raise Exception
                validador = 0
            except(Exception):
                print("CPF inválido. Digite novamente.\n")
    
    def receber_dados(self):
        self.receber_nome()
        self.receber_idade()
        self.receber_cpf()
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}")

if __name__ == '__main__':
    pessoas = []
    for id in range(3):
        pessoas.append(Pessoa())
        print(f"Pessoa {id+1}\n")
        pessoas[id].receber_dados()
    
    for id in range(3):
        print(f"Pessoa {id+1}\n")
        pessoas[id].mostrar_dados()


        