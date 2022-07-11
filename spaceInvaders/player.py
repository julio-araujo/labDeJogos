from PPlay.gameimage import *
from PPlay.window import *
from PPlay.sprite import *


def movimento(teclado,nave,velNave,janela):
    if teclado.key_pressed("LEFT") and nave.x > 0:
        return nave.move_x(-velNave)
    if teclado.key_pressed("RIGHT") and nave.x < janela.width - nave.width:
        return nave.move_x(velNave)
    return None
