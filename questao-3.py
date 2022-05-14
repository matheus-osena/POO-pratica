"""3. **Modifique o programa anterior para que não seja possível cadastrar duas pessoas com o mesmo CPF. 
Ao cadastrar um CPF já existente, o programa deverá avisar que o CPF está repetido 
e pedir para que o usuário entre com os dados novamente.*****"""


class Pessoa():

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

class Cadastro():

    def __init__(self):
        self.pessoas = []
        self.conjunto_cpfs = set()
        self.quant_pessoas = None
    
    #altera o atributo de quant_pessoas
    def quantidade_de_pessoas(self):
        validador = 1
        while validador == 1:
            try:
                self.quant_pessoas = int(input("Digite a quantidade de pessoas: \n"))
                validador = 0
            except(Exception):
                print("Esse campo deve conter somente números. Digite novamente: \n")

    def cadastro_geral(self):
        self.quantidade_de_pessoas()
        for id in range(self.quant_pessoas):
            try:
                numero_de_cpfs = len(self.conjunto_cpfs)
                self.pessoas.append(Pessoa())
                self.pessoas[id].receber_dados()
                self.conjunto_cpfs.add(self.pessoas[id].cpf)
                if numero_de_cpfs == len(self.conjunto_cpfs):
                    raise Exception
            except(Exception):
                validador = 1
                while validador == 1:
                    print("CPF já cadastrado. Digite os dados novamente:\n")
                    self.pessoas[id].receber_cpf()
                    self.conjunto_cpfs.add(self.pessoas[id].cpf)
                    validador = 0
                    if numero_de_cpfs == len(self.conjunto_cpfs):
                        validador = 1
    
    def mostrar_cadastro(self):
        for pessoa in self.pessoas:
            pessoa.mostrar_dados()




if __name__ == '__main__':
    cadastro = Cadastro()
    cadastro.cadastro_geral()
    cadastro.mostrar_cadastro()
