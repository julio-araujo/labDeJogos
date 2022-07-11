from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *


def verificarPipoco(tiros,monstros,pBoss,vidaBoss,pontos):
    l=0
    for linha in monstros:
        c=0
        for monstro in linha:
            for tiro in tiros:    
                if tiro.collided(monstro):
                    if (l,c)==pBoss and vidaBoss:
                        vidaBoss-=1
                        tiros.remove(tiro)
                    elif l==pBoss[0]:
                        if c<pBoss[1]:
                            c-=1
                            pBoss=(l,pBoss[1]-1)
                        tiros.remove(tiro)
                        linha.remove(monstro)
                        pontos+=5
                    else:
                        tiros.remove(tiro)
                        linha.remove(monstro)
                        pontos+=5
                if linha==[]:
                    monstros.remove(linha)
                    break
            c+=1
        l+=1
    return vidaBoss,pontos,pBoss

def verificaPlayerHit(tirosMonstros,player,janela,inv):
    if inv<3:
        return False
    else:
        for tiro in tirosMonstros:
            if tiro.collided(player):
                player.x = janela.width/2
                tirosMonstros.remove(tiro)
                return True
            else:
                return False