deposito = 0
saque = 0
extrato = 0
relatorio_deposito = ""
relatorio_saque = ""
total_saque = 0
limite_saques = 0


menu = '''
==================================== MENU =========================================

            1 - Deposito:

            2 - Saque:

            3 - Extrato:

            4 - Sair:

=================================================================================== 

Escolha uma das Opções: '''

while True:

    opcao = int(input(menu))

    if opcao == 1:
        while True:

            novo_deposito = float(input('''
            Insira o valor a ser depositado: '''))
            
            deposito += novo_deposito

            if novo_deposito > 0:
                
                relatorio_deposito += f'''
            Valor de Deposito: R$ {novo_deposito:.2f}\n\n'''

                print(f'''
===================================================================================                
            
            Deposito Comfirmado 
            
            No valor de R${novo_deposito:.2f}

            Saldo atualizado para R${deposito:.2f}

===================================================================================
            ''')
                break
            else: print("\n\n           Deposito Interronpido, não é possivel deposito um valor abaixo de R$ 0.00")    


    elif opcao == 2:



        if limite_saques < 3:
            

            saque = float(input('''
            Informe o valor que deseja sacar: R$ '''))
            
            if saque <= 500:
                if deposito >= saque:
                    deposito -= saque
                    print('''
____________________________________________________________________________________
                                        
            Saque realizado com sucesso

____________________________________________________________________________________
                        ''')
                    total_saque+= saque
                    relatorio_saque += f'''
            Valor de Saque: R$ {saque:.2f}
'''
                    limite_saques +=1
                else: print(f"\n\n          Saldo Insuficiente\n            Saldo atual: R$ {deposito:.2f}")    
            else: print("\n\n           O limite maximo de saque é áte R$ 500.00 por operação")
        else: print("\n\n           Você atigio o limite de 3 saques diarios")    

    elif opcao == 3:
        print(f'''
            Extrato:

            Relatorio de Deposito:
            {relatorio_deposito}
            Saldo atual da Conta: R${deposito:.2f}

            Relatorio de Saque:
            {relatorio_saque}
            ''')

    elif opcao == 4:
        print("Programa Encerrado")
        break
    
    else: print("Operação invalida, por favor selecione novamente a operação desejada")
