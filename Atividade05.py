from abc import ABC, abstractmethod
import os

os.system("cls || clear")


class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
        )

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float , endereco: Endereco ) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.Endereco = endereco

    @abstractmethod
    def salario_final(self) -> float: 
        pass

    def  __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.Endereco}"
            f"\nSalário: R$ {self.salario}"
            f"\nSalário final: R$ {self.salario_final()}" 
            )
class Engenheiro(Funcionario):
    BONIFICACAO = 1.3
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)    
        self.crea = crea 

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado    
    def __str__(self) -> str:
        return (f"{super().__str__()}"  
                f"\nCREA: {self.crea}"
                )   


class Medico (Funcionario): 
    BONIFICACAO = 1.5
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, cfm: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)   
        self.cfm = cfm 
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCFM: {self.cfm}"
                )
    
engenheiro = Engenheiro("Samir", "(71)91234-5678", "samirsantos@gmail.com", 6000, Endereco("Rua A","12","Perto da padaria","123.45-000","Salvador"),"2034-8" )
medico = Medico("Rafael", "(71) 98765-4321","rafaeldias@gmail.com", 6000, Endereco("Rua B","07","Perto de Sr. zé","987.43-0000","Rio de janeiro"),"546-0")

print(engenheiro)
print(medico)