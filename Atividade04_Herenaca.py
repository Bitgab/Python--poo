from abc import ABC, abstractmethod
import os

os.system("cls || clear")

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    @abstractmethod   # Decoradaor 
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nSalário: R$ {self.salario}"
            f"\nSalário final: R$ {self.salario_final()}"
        )
class Motoboy(Funcionario):
    #ACRÉSCIMO DE 10%
    BONIFICACAO = 1.1

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

class Engenheiro(Funcionario):
    #ACRÉSCIMO de 20%.
    BONIFICACAO = 1.2
    def __init__(self, nome: str, salario: float, crea: str) -> None:
        super().__init__(nome, salario)
        self.crea = crea

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado 
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}" 
                )   
    
class Medico(Funcionario):
    #ACRÉSCIMO 20%
    BONIFICACAO = 1.3
    def __init__(self, nome: str, salario: float, cfm:str) -> None:
        super().__init__(nome, salario)
        self.cfm = cfm
    
    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO   
        resultado = self.salario * self.BONIFICACAO
        return resultado
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCFM: {self.cfm}"
                )

# Instanciando Classes.
motoboy_1 = Motoboy("Jose", 1000)
engenheiro = Engenheiro("Sergio", 2000, "1234-5")
medico = Medico("Selline", 6000, "234-5")

print(motoboy_1)
print(engenheiro)
print(medico)