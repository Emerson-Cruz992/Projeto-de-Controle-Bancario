def menu():
    menu = """\n
    =========== MENU ===========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuario
    [7] Sair
    
    =>"""
    return menu

def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def saque_conta(*, saldo, limite, valor, numero_saque, limite_saque, extrato):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saque >= limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saque += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato_conta(saldo,/, *, extrato,):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtra_usuario(usuarios, cpf):

    for usuario in usuarios:

        if usuario["cpf"] == cpf:
            print(type(usuario))
            return usuario
    
    return None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente numeros): ")
    usuario = filtra_usuario(usuarios, cpf)

    if usuario:
        print("Usuario já cadastrado com esse cpf: ")
        return
    
    
    nome = input("Qual o sue nome: ")
    data_de_nascimento = input("Qual a data de nascimento (dia/mes/ano): ")
    endereco = input("Informe se endereço (logradouro, numero - bairro - cidade/sigla estado):\n >>> ")

    usuarios.append({"nome": nome, "data_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereco})

    print(">>>> Usuario Criado com sucesso! <<<<")

def criar_conta(numero_conta, agencia, usuarios):
    cpf = input("Informe seu cpf (somente numeros): ")
    verificação_usuario = filtra_usuario(usuarios, cpf)

    if verificação_usuario:
        print("### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": verificação_usuario}
        
    
    print("\n>>> Usuario não encontrado, processo de criação de conta encerrada.")
    

def lista_contas(contas):

    for conta in contas:
        texto = f"""\n
        Agência: {conta["agencia"]}
        N. conta: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
"""
        print(texto)

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []


    while True:
        print(menu())
        opcao = input()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor de Saque: "))

            saldo, extrato = saque_conta(
                saldo=saldo, 
                limite=limite, 
                valor=valor, 
                numero_saque=numero_saque, 
                limite_saque=LIMITE_SAQUES, 
                extrato=extrato)
            
        elif opcao == "3":
            extrato_conta(saldo, extrato=extrato)

        elif opcao == "4":

            numero_da_conta = len(contas) + 1
            conta = criar_conta(numero_da_conta, AGENCIA, usuarios)
            
            if conta: 

                contas.append(conta)

        elif opcao == "5":

            lista_contas(contas)
        
        elif opcao == "6":

            criar_usuario(usuarios)
            
        elif opcao == "7":
            break
        else: 
            print("Opção invalida, por favor escolha novamente.")
            
main()
