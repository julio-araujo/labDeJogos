from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from monstros import *
from player import *
from colisões import *
from random import randint

def jogo(janela,dif,teclado,fundo,round,pontos):
    nave=Sprite("nave.png")
    vida=3
    inv=0
    dTempo=0
    fps=0
    contFrame=0
    tiros=[]
    tirosMonstros=[]
    contTiroInimigo=0
    qtdMaxMonstroLargura=janela.width* (0.7)  # conf difilculdade = alterar 0.7 por numero maior
    qtdMaxMonstroAltura=janela.height*(0.5)
    nave.y=janela.height-nave.height-10
    nave.x=janela.width/2
    velNave=2
    velMonstroX = int(janela.width / 600)*dif
    velMonstroY = int(janela.height / 100)*dif
    contMove=0
    contTiro=1
    monstros,pBoss = criarListaMonstro(qtdMaxMonstroLargura,qtdMaxMonstroAltura)
    vidaBoss = 3
    while True:
        movimento(teclado,nave,velNave,janela)
        if teclado.key_pressed("esc"):
            return False,pontos
        if teclado.key_pressed("space") and contTiro>0.5:
            contTiro=0
            tiro=Sprite("tiro.png")
            tiro.x=nave.x+(nave.width/2)
            tiro.y=nave.y
            tiros.append(tiro)
        for i in tiros:
            if (i.y <= 0):
                tiros.remove(i)
            else:
                i.y-=3
        for i in tirosMonstros:
            if i.y > janela.height:
                tirosMonstros.remove(i)
            else:
                i.y+= 3
        if monstros == []:
            # confifurações apos todos os inimigos serem eliminados
            return True,pontos  
        if contMove >= 1:
            velMonstroX=movimentoRmonstros(monstros,janela,velMonstroX,velMonstroY)
            contMove=0
        #monstro atirar
        if contTiroInimigo > 1:
            atirarMonstro(monstros,tirosMonstros)
            contTiroInimigo = 0
        #conta os frames e caso se passe 1 Segundo, atualiza a quantidade de fps
        dTempo+=janela.delta_time()
        contFrame+=1
        if dTempo >= 1:
            fps = contFrame
            contFrame=0
            dTempo=0
        if verificaPlayerHit(tirosMonstros,nave,janela,inv):
            vida -= 1
        if vida == 0 or monstroBaixo(monstros) >= nave.y:
            #conf apos player morrer
            return False,pontos
        vidaBoss,pontos,pBoss=verificarPipoco(tiros,monstros,pBoss,vidaBoss,pontos)
        fundo.draw()
        for k in tiros:
            k.draw()
        for k in tirosMonstros:
            k.draw()
        desenhaMonstros(monstros)
        nave.draw()
        janela.draw_text(str(fps), 5, 5, 25, (255, 255, 255), "arial", False, False)
        janela.draw_text(str(vida), janela.width-30 , 5, 25, (255, 255, 255), "arial", False, False)
        janela.draw_text(str(round)+ " "*5 +str(pontos), (janela.width-30)/3 , 5, 25, (255, 255, 255), "arial", False, False)
        inv += janela.delta_time()
        contTiroInimigo += 1 * janela.delta_time()
        contTiro+= 1 * janela.delta_time()
        contMove+= 100 * janela.delta_time()
        janela.update()