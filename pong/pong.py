from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *

contDireito=contEsquerdo=0
janela = Window(600, 504)
janela.set_title('Ping Pong')
teclado=Window.get_keyboard()
mouse = Window.get_mouse()
fundo = GameImage("mesaPing.png")
bola = Sprite("ball.png", 1)
padDir=Sprite("padDir.png",1)
padEsq=Sprite("padEsq.png",1)

velZero=0

velX = 300
velY = 111
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

padEsq.x=10
padEsq.y=janela.height/2

padDir.x=janela.width-padDir.width-10
padDir.y=janela.height/2 - padDir.height/2
velPad=300

while True:
    # update-fisica
    # move bola
    bola.move_x(velX*janela.delta_time())
    bola.move_y(velY*janela.delta_time())

    #move pads

        #teclado
    if teclado.key_pressed("UP") and padDir.y>0:
        padDir.move_y(-velPad*janela.delta_time())
    if teclado.key_pressed("DOWN") and padDir.y < janela.height-padDir.height:
        padDir.move_y(velPad * janela.delta_time())
    # IA controlando pad esq
    if bola.x < janela.width/2:
        if bola.y > padEsq.y:
            padEsq.move_y(100*janela.delta_time())
        if bola.y < padEsq.y:
            padEsq.move_y(-100*janela.delta_time())
    '''
        #mouse
    if janela.height-padEsq.height > mouse.get_position()[1]>0:
        padEsq.y=mouse.get_position()[1] # -(padEsq.y/2)
    '''
    # colisão
    if (bola.y < 0): #bola parede sup
        velY = velY * (-1)
        bola.y= 0
    if (bola.y+bola.height > janela.height): #bola parede inf
        velY= velY * (-1)
        bola.y=janela.height-bola.height
    if bola.collided(padDir): #bola com pad dir.
        velX = velX * (-1)
        bola.x =  padDir.x-bola.width-1
    if bola.collided(padEsq): #bola com pad esq.
        velX = velX * (-1)
        bola.x = padEsq.x+padEsq.width+1
    #att pontuação (contador) e reiniciar as variaveis
    if bola.x> janela.width:
        contEsquerdo+=1
        
        
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        

        padEsq.x = 10
        padEsq.y = janela.height / 2
        padDir.x=janela.width-padDir.width-10
        padDir.y=janela.height/2 - padDir.height/2
        
        """
        trava=True
        bola.x=padEsq.x+1+(padEsq.width)/2
        while trava:
            bola.y=padEsq.y-(padEsq.height)/2
            if teclado.key_pressed("SPACE"):
                trava=False
        """
    
    if bola.x < 0:
        contDireito += 1
        
        
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        
        
        padEsq.x = 10
        padEsq.y = janela.height / 2
        padDir.x=janela.width-padDir.width-10
        padDir.y=janela.height/2 - padDir.height/2
        
        trava=True
        bola.x=padDir.x-1-(padDir.width)/2
        while trava:
            bola.y=padDir.y+(padDir.height)/2
            if teclado.key_pressed("SPACE"):
                trava=False
            if teclado.key_pressed("UP") and padDir.y>0:
                padDir.move_y(-velPad*janela.delta_time())
            if teclado.key_pressed("DOWN") and padDir.y < janela.height-padDir.height:
                padDir.move_y(velPad * janela.delta_time())
            fundo.draw()
            janela.draw_text(str(contDireito),janela.width*(3/4),15,50,(255,255,255),"Arial",True)
            janela.draw_text(str(contEsquerdo),janela.width/4,15,50,(255,255,255),"Arial",True)
            bola.draw()
            padDir.draw()
            padEsq.draw()
            janela.update()


    fundo.draw()
    janela.draw_text(str(contDireito),janela.width*(3/4),15,50,(255,255,255),"Arial",True)
    janela.draw_text(str(contEsquerdo),janela.width/4,15,50,(255,255,255),"Arial",True)
    bola.draw()
    padDir.draw()
    padEsq.draw()
    janela.update()