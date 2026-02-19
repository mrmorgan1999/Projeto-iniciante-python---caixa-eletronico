import sys
import random

print ("bem vindo ao pedra papel tesoura")
print ()

            
def finalizar ():
    sys.exit("programa finalizado")

def regras ():
    print ()
    print ("pedra ganha de tesoura") 
    print ("tesoura ganha de papel") 
    print ("papel ganha de pedra") 
    print ("caso de igual ninguem ganha ponto")
    print ()
    while True:
        try:
         continuarregras = int (input("digite 1 para voltar pro menu ou 2 pra sair do programa: "))
        except ValueError:
            print ("resposta nao reconhecida, responda com numeros inteiros")
            continue
            
        if continuarregras == 1:
          break
        elif continuarregras == 2:
             finalizar ()
        else:
             print ("resposta nao reconhecida")      

def jogar ():
    v1 = 0
    v2 = 0
    partida = 1
    rodada = 1
    print ()
    print ("sao 5 rodadas, quem tiver mais vitorias ganha, empate nao conta rodada")
    print ("1.tesoura")
    print ("2.papel")
    print ("3.pedra")
    while rodada < 6:
        print ()
        print (f"{partida}. rodada")
        while True:  
         try:
            jogador = int (input("escolha uma opçao: "))
            if (jogador == 1) or (jogador == 2) or (jogador == 3):
                break
            else:
                print ("resposta nao reconhecida")
         except:
            print ("resposta nao reconhecida, responda com numeros inteiros")
            
        opcoes = ['pedra','papel','tesoura']  
        oponente = random.choice(opcoes)
        
        
        print (f"o seu oponente escolheu: {oponente}")
        
        if jogador == 1:
            escolhajogador = "tesoura"
        elif jogador == 2:
            escolhajogador = "papel"
        else:
            escolhajogador = "pedra"
            
        if ((oponente == "pedra") and (escolhajogador == "tesoura")) or ((oponente == "tesoura") and (escolhajogador == "papel")) or ((oponente == "papel") and (escolhajogador == "pedra")):
            print ("voce perdeu esta rodada")
            rodada = rodada + 1
            v1 = v1 + 1
        elif oponente == escolhajogador:
            print ("empatou nessa rodada (nao conta)")
        else:
            print ("voce ganhou essa rodada")
            rodada = rodada + 1
            v2 = v2 + 1
        partida = partida + 1  
    if rodada == 6:
        if v1 > v2:
            print("fim de partida voce perdeu")
        else:
            print ("fim de partida voce ganhou")
        
        

def menu ():
 while True:
    print ()
    print ("1.jogar")
    print ("2.regras")
    print ("3.sair")
    while True:  
     try:
         resposta = int (input("escolha uma opçao: "))
         if (resposta == 1) or (resposta == 2) or (resposta == 3):
             break
         else:
             print ("resposta nao reconhecida")
     except:
         print ("resposta nao reconhecida, responda com numeros inteiros")
         
    if resposta == 1:
        jogar ()
    elif resposta == 2:
        regras()
    else:
        finalizar()
    
menu ()