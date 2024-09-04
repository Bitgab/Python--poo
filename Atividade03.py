import os 
os.system("cls || clear") # Limpa o terminal

# Criando a classe Conta Bancaria.
class ContaBancaria:
    #Criando um construtor.
    def __init__(self, banco: str, agencia: str, numeroDaconta: str, tipoDaConta: str, saldoAtual: str, limiteDisponivel: str) -> None:
        self.banco = banco
        self.agencia = agencia
        self.numeroDaConta = numeroDaconta
        self.tipoDaConta = tipoDaConta
        self.saldoAtual = saldoAtual
        self.limiteDisponivel = limiteDisponivel
    #Semelhante ao toString()
    def __str__(self) -> str:
        return (
            f"\nBanco: {self.banco} "
            f"\nAgência: {self.agencia}"
            f"\nNúmero da conta: {self.numeroDaConta}"
            f"\nTipo da conta: {self.tipoDaConta}"
            f"\nSaldo atual: R$ {self.saldoAtual} "
            f"\nLimite disponível: R$ {self.limiteDisponivel}"
            )

# Criando a classe Endereço.    
class Endereco: 
    #Criando um construtor.
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
    #Semelhante ao toString()
    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\ncidade: {self.cidade}"
            )

# Criando a classe Funcionário.
class Funcionario: 
    #Criando um construtor.
    def __init__(self, codigoDoFuncionario: str, nome: str, endereco: Endereco, telefone: str, email: str, contaBanco: ContaBancaria) -> None:
        self.codigoFuncionario = codigoDoFuncionario
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.contaBanco = contaBanco       
         
    #Semelhante ao toString()
    def __str__(self) -> str:
        return (
            f"\nCódigo do funcionário: {self.codigoFuncionario}"
            f"\nNome: {self.nome}"
            f"\nEndereço: {self.endereco}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nConta banco: {self.contaBanco}"           
            )
endereco = Endereco("Rua A", "7", "Salvador")
conta = ContaBancaria("Inter","1234", "00002345-67", "Conta Poupança", "5000", "4900")       
funcionario = Funcionario("012", "Fuboca", endereco, "(71) 91234-5678", "fuboca@gmail.com", conta)

print (funcionario)