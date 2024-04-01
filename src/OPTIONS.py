from screeninfo import *

class OPTIONS:

    """
    Cette classe renseigne les options du jeu
    """

    SOUND_ON = True
    KEYS = ()

    def switch_sound(cls):
        if cls.SOUND_ON:
            cls.SOUND_ON = False
        else: cls.SOUND_ON = True
    switch_sound = classmethod(switch_sound)

class SCREENINFO:

    """
    Cette classe renseigne les options de la fenetre du jeu
    """

    FULLSCREEN = True
    RES = (720, 450)
    if FULLSCREEN:
        RES = get_monitors()[0].width, get_monitors()[0].height
    FPS = 60

    def switch_FULLSCREEN(cls):
        if cls.FULLSCREEN:
            cls.FULLSCREEN = False
        else: cls.FULLSCREEN = True
    switch_FULLSCREEN = classmethod(switch_FULLSCREEN)

    def set_RES(cls, resolution:tuple):
        if cls.FULLSCREEN:
            cls.RES = get_monitors()[0].width, get_monitors()[0].height
        else : cls.RES = resolution
    set_RES = classmethod(set_RES)