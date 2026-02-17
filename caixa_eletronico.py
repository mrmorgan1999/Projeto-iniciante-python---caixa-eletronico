import sys
print ("............CAIXA ELETRONICO DO BRASIL............")
def end ():
    print ("programa finalizado")
    sys.exit()

def finalizar (frs):
    resp = input (frs)
    while True:
        if resp == "nao":
            end()
        elif resp == "sim":
            print ("prosseguindo....")
            break
        else:
            resp = input ("resposta nao entendida responda (sim) ou (nao): ")

frase = "deseja entrar no sistema?: "            
finalizar (frase)

print ("..........BEM VINDO AO SISTEMA DE CAIXA ELETRONICO DO BRASIL..........")

def senha (senha_user):
    print ("digite a senha, caso erre a senha 3 vezes o seu acesso sera bloqueado: ")
    cont = 0
    while True:
        resp1 = int (input("digite a senha: "))
        if resp1 != senha_user:
            print("senha errada digite novamente: ")
            if cont == 2:
                print ("limite de tentativas alcançada...")
                end ()
            cont = cont + 1
        else:
            print ("senha correta, prosseguindo....")
            break

senha (2010)            

saldo = 1000

def menu ():
    print()
    print ("MENU BANCARIO..............")
    print(F"SALDO: {saldo:.2f} R$")
    print ("SAQUE...................[1]")
    print ("DEPOSITO................[2]")
    print ("FINALIZAR PROGRAMA......[3]")
    print ("HISTORICO DE TRANSAÇAO..[4]")
    print (".........SAQUES ACIMA DE 300$ TERAO UMA TAXA DE 10%.........")
    print

valor_transaçoes = []
def historico (valor,tipo):
    valor_transaçoes.append(f"{tipo} de {valor} R$")
    
def extrato ():
    for i in range (len(valor_transaçoes)):
        print(f"{i+1}. {valor_transaçoes[i]}")
      
def deposito ():
    global saldo
    while True:
                deposito = float (input("Quanto voce deseja depositar? (valor maximo de deposito é 500$) "))
                if (deposito <= 0) or (deposito > 500) :
                    print ("nao é possivem fazer um deposito com esse valor")
                else: 
                    print ("deposito realizado com sucesso") 
                    saldo = saldo + deposito
                    tip = "deposito"
                    historico(deposito,tip)
                    break

lim = 0

def saque ():
    global lim
    global saldo
    while True:
                saque = float (input("digite o valor do saque (valor maximo por saque é 500$) "))
                if (saque > saldo) or (saque <= 0) or ( saque > 500):
                    print ("nao é possivel realizar um saque com esse valor")
                else:
                    if saque < 300:
                        print ("saque realizado com sucesso")
                        saldo = saldo - saque
                        lim = lim + 1
                        tip = "saque"
                        historico(saque,tip)
                        break
                    else:
                        taxa = saque*0.10
                        ff = saque + taxa
                        if ff > saldo:
                            print ("nao é possivel realizar esse saque devido a taxa de saque, que faz tal transaçao passar do seu saldo")
                        else:
                            print (f"saque realizado com sucesso, taxa de {taxa:.2f} R$")
                            saldo = saldo - ff
                            lim = lim + 1
                            tip = "saque"
                            historico(ff,tip)
                            break
                        

    
def escolha ():
    while True: 
        esc = int (input("Escolha uma opçao: "))
        if esc == 2:
            deposito ()
            break      
        elif esc == 1:
            if lim == 3:
                print ("limite de saque alcançado, volte amanha")
            else:
                saque ()
                break
        elif esc == 3:
            end ()
        elif esc ==4:
            if not valor_transaçoes:
                print("nao existe nenhum historico de transaçao")
            else:
                extrato ()
        else:
            print ("opçao invalida")
            
while True:
    menu ()
    escolha ()
            

    