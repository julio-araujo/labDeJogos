from re import T
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from principal import *
from colisões import *
from monstros import *
from player import *

janela = Window(900,600)
janela.set_title("Space Invaders")
fundo = GameImage("fundoSpace.png")

bInicio=Sprite("bInicio.jpg")
bDificuldade=Sprite("bDificuldade.jpg")
bFacil=Sprite("bFacil.jpg")
bMedio=Sprite("bMedio.jpg")
bDif=Sprite("bDificil.jpg")
bRank=Sprite("bRank.jpg")
bSair=Sprite("bSair.jpg")
nave=Sprite("nave.png")
dif=1

"""
tiros=[]


velMonstroX = int(janela.width / 600)*dif
velMonstroY = int(janela.height / 100)*dif

nave.y=janela.height-nave.height-10
nave.x=janela.width/2
velNave=2
"""

bInicio.x=(janela.width/2)-(bInicio.width/2)
bInicio.y=(janela.height/4)

bDificuldade.x=(janela.width/2)-(bDificuldade.width/2)
bDificuldade.y=(janela.height/4)+50

bFacil.x=(janela.width/6)
bFacil.y=(janela.height/4)

bDif.x=(janela.width/6)+bFacil.width+50
bDif.y=(janela.height/4)-50-bMedio.height

bMedio.x=bDif.x+50+bDif.width
bMedio.y=(janela.height/4)

bRank.x=(janela.width/2)-(bRank.width/2)
bRank.y=(janela.height/4)+100

bSair.x=(janela.width/2)-(bSair.width/2)
bSair.y=(janela.height/4)+150

mouse = Window.get_mouse()
teclado=Window.get_keyboard()

"""
#contTiro=1
#contMove=0
#qtdMaxMonstroLargura=janela.width* (0.7)  # conf difilculdade = alterar 0.7 por numero maior
#qtdMaxMonstroAltura=janela.height*(0.5)
"""

while True:
    # teclado
    if mouse.is_over_object(bInicio) and mouse.is_button_pressed(1):
            round=1
            pontos=0
            controle,pontos=jogo(janela,dif,teclado,fundo,round,pontos)
            while controle:
                round+=1
                controle,pontos=jogo(janela,dif,teclado,fundo,round,pontos)
                janela.update()
            
            nomeJogador= input()
            dados = open("ranking.txt","r")
            ranking = dados.readlines()
            for classificado in range(len(ranking)):
                aux=ranking[classificado].strip().split("#")
                ranking[classificado] = [int(aux[0]),aux[1]]
            dados.close()
            ranking.append([pontos,nomeJogador.lower()])
            
            dados = open("ranking.txt","w")
            for classificado in sorted(ranking, reverse=True)[0:9]:
                dados.write(str(classificado[0])+"#"+classificado[1]+"\n")
            dados.close()
            janela.update()

            """
            monstros=criarListaMonstro(qtdMaxMonstroLargura,qtdMaxMonstroAltura)
            while True:
                movimento(teclado,nave,velNave,janela)
                if teclado.key_pressed("esc"):
                    break
                if teclado.key_pressed("space") and contTiro>0.5:
                    contTiro=0
                    tiro=Sprite("tiro.png")
                    tiro.x=nave.x+(nave.width/2)-7
                    tiro.y=nave.y
                    tiros.append(tiro)
                for i in tiros:
                    if (i.y <= 0):
                        tiros.remove(i)
                    else:
                        i.y-=3
                fundo.draw()
                for k in tiros:
                    k.draw()
                if contMove >=1:
                    controle=movimentoRmonstros(monstros,janela,velMonstroX,velMonstroY)
                    if controle == False:
                        break
                    else:
                        velMonstroX=controle
                    contMove=0
                desenhaMonstros(monstros)
                nave.draw()
                contTiro+= 1 * janela.delta_time()
                contMove+=100*janela.delta_time()
                verificarPipoco(tiros,monstros)
                janela.update()
                """
    
    if mouse.is_over_object(bDificuldade) and mouse.is_button_pressed(1):
        while True:
            fundo.draw()
            bFacil.draw()
            bMedio.draw()
            bDif.draw()
            janela.update()
            if mouse.is_over_object(bFacil) and mouse.is_button_pressed(1):
                # codigo q faz as alteraçoes para essa dificuldade
                dif=1
                velMonstroX = int(janela.width / 600)*dif
                velMonstroY = int(janela.height / 100)*dif
                velNave = 1/dif
                break
            if mouse.is_over_object(bMedio) and mouse.is_button_pressed(1):
                # codigo q faz as alteraçoes para essa dificuldade
                dif=1.3
                velMonstroX = int(janela.width / 600)*dif
                velMonstroY = int(janela.height / 100)*dif
                velNave = 1/dif
                break
            if mouse.is_over_object(bDif) and mouse.is_button_pressed(1):
                # codigo q faz as alteraçoes para essa dificuldade
                dif=1.5
                velMonstroX = int(janela.width / 600)*dif
                velMonstroY = int(janela.height / 100)*dif
                velNave = 1/dif
                break
    if mouse.is_over_object(bRank) and mouse.is_button_pressed(1):
        while True:
            dados = open("ranking.txt","r")
            ranking = dados.readlines()
            dados.close()
            xNome,xPonto,y = 20, 300, 10
            fundo.draw()
            janela.draw_text("press esc to go back", janela.width/2, janela.height-50, 30 , (255, 255, 255), "arial", False, False)
            for dadosJogador in ranking:
                ponto,nome=map(str,dadosJogador.strip().split("#"))
                janela.draw_text(str(nome), xNome,y ,30 ,(255, 255, 255), "arial", False, False)
                janela.draw_text(str(ponto), xPonto, y, 30 , (255, 255, 255), "arial", False, False)
                y+=30
            janela.update()
            if teclado.key_pressed("esc"):
                break    
    if mouse.is_over_object(bSair) and mouse.is_button_pressed(1):
        break
    #draw
    fundo.draw()
    bInicio.draw()
    bDificuldade.draw()
    bRank.draw()
    bSair.draw()
    janela.update()