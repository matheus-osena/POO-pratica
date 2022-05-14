"""2. **Modifique o programa anterior para ler dados de um número variável de pessoas. 
O programa deverá ler primeiramente o número de pessoas (n) e posteriormente ler os dados das pessoas. 
Por fim, o programa deve exibir a lista de pessoas.***"""

def quantidade_de_pessoas():
        n = int(input("Digite a quantidade de pessoas que serão cadastradas:\n"))
        return n

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
    quantidade_de_pessoas = quantidade_de_pessoas()
    pessoas = []
    for id in range(quantidade_de_pessoas):
        pessoas.append(Pessoa())
        print(f"Pessoa {id+1}\n")
        pessoas[id].receber_dados()
    
    for id in range(quantidade_de_pessoas):
        print(f"Pessoa {id+1}\n")
        pessoas[id].mostrar_dados()


        