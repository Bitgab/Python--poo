import os
os.system("cls || clear") # Limpa o terminal

# Criando a classe Endereço.
class Endereco:
    #Criando um construtor. o Construto.
    def __init__(self, logradouro: str, numero: str) -> None:      
        self.logradouro = logradouro
        self.numero = numero 
    #Semelhante ao toString()                           
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            )    


class Cliente:  
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self) -> str: 
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"
    
# Instanciar classe.
endereco1 = Endereco("Rua A", "12")
cliente = Cliente("Fuboca", "22", endereco1)                                
   
print(cliente.exibir_dados())   