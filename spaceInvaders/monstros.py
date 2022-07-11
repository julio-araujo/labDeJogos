from pyparsing import col
from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *
from random import randint

def criarListaMonstro(qtdMaxlargura,qtdMaxAltura):
    monstros=[]
    x = ((qtdMaxlargura / 0.7) * 0.3) / 2  # ajustar dificuldade = alterar 0.7
    y = 10
    xMax = int(qtdMaxlargura/ Sprite("inimigo.png").width)
    yMax= int(qtdMaxAltura/Sprite("inimigo.png").height)
    p=(randint(0,yMax-1),randint(0,xMax-1))
    for i in range(yMax):
        aux = []
        for j in range(xMax):
            if p==(i,j):
                monstro = Sprite("boss.png")
            else:
                monstro = Sprite("inimigo.png")
            monstro.set_position(x,y)
            aux.append(monstro)
            x += monstro.width * (5 / 4)
        monstros.append(aux[:])
        y += aux[0].height * (5 / 4)
        x = ((qtdMaxlargura / 0.7) * 0.3) / 2
    return monstros,p

def movimentoRmonstros(monstros,janela,velx,vely):
    #pega localiazção dos monstros extremos
    inicio,fim=monstroLado(janela,monstros)
    #verifica caso o monstra tenha saido pela esqueda (e trata)
    if inicio<0:
        velx*=-1
        for i in monstros:
            for j in i:
                j.x-=inicio
                j.y+=vely
    #verifica caso o monstra tenha saido pela direita (e trata)
    elif fim > janela.width:
        velx*=-1
        for i in monstros:
            for j in i:
                j.x-=(fim-janela.width)
                j.y+=vely
    #anda com os monstros caso n haja colisão 
    else:
        for i in monstros:
            for j in i:
                j.x+=velx
    return velx

def atirarMonstro(monstros, tirosMonstros):
    lin=randint(0,len(monstros)-1)
    col=randint(0,len(monstros[lin])-1)
    tiro = Sprite("tiro.png")
    tiro.x= monstros[lin][col].x + monstros[lin][col].width/2
    tiro.y= monstros[lin][col].y
    tirosMonstros.append(tiro)
    return None

def monstroLado(janela,monstros):
    inicio=janela.width
    fim=0
    for i in monstros:
            for j in i:
                if j.x+j.width>fim:
                    fim=j.x+j.width
                if j.x<inicio:
                    inicio=j.x
    return inicio,fim
    
def monstroBaixo(monstros):
    return monstros[-1][0].y+monstros[-1][0].height

def monstroCima(monstros):
    return monstros[0][0].y


def desenhaMonstros(monstros):
    for linha in monstros:
        for monstro in linha:
            monstro.draw()
    return None