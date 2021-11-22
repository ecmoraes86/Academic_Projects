def computador_escolhe_jogada(n,m):
    computador_retira = n%(m+1)
    return computador_retira
    

def usuario_escolhe_jogada(n,m):
    usuario_retira = 0
    while usuario_retira < 1 or usuario_retira > m or usuario_retira > n:
        usuario_retira = int(input("Quantas peças você vai tirar? "))

        if usuario_retira < 1 or usuario_retira > m or usuario_retira > n:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return usuario_retira


def partida():
    n=0
    m=0
    while(n<1 or m<1):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        if n<1 or m<1:
            print("Oops! Quantidade de peças e limite de pelas por jogada devem ser um número maior ou igual a 1! Tente de novo.")


    if n%(m+1)==0:
        print("Você começa!")
        while n>0:
            usuario_retira = usuario_escolhe_jogada(n,m)

            if usuario_retira == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",usuario_retira,"peças.")

            n = n - usuario_retira

            if n==0:
                print("Fim do jogo! Você ganhou!")
                return 1
            elif n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")

            computador_retira = computador_escolhe_jogada(n,m)
            
            if  computador_retira == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", computador_retira,"peças.")

            n = n -  computador_retira

            if n==0:
                print("Fim do jogo! O computador ganhou!")
                return 0
            elif n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")

    else:
        print("Computador começa!")
        while n>0:
            computador_retira = computador_escolhe_jogada(n,m)
            
            if  computador_retira == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", computador_retira,"peças.")

            n = n - computador_retira

            if n==0:
                print("Fim do jogo! O computador ganhou!")
                return 0
            elif n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")

            usuario_retira = usuario_escolhe_jogada(n,m)

            if usuario_retira == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou",usuario_retira,"peças.")

            n = n - usuario_retira

            if n==0:
                print("Fim do jogo! Você ganhou!")
                return 1
            elif n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n,"peças no tabuleiro.")

    
def campeonato():
    i=1
    computador = 0
    usuario = 0
    while(i<=3):
        print("**** Rodada",i,"****")
        resultado = partida()
        if resultado == 0:
            computador = computador + 1
        else:
            usuario = usuario + 1
        i = i + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você",usuario,"X",computador,"Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("1 - para jogar uma partida isolada")
    menu = int(input("2 - para jogar um campeonato "))

    if menu==1:
        print("Você escolheu uma partida isolada!")
        partida()

    elif menu==2:
        print("Você escolheu um campeonato!")
        campeonato()

    else:
        print("Jogo encerrado")

main()
