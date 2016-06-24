from sprite import LcarsWidget
import pygame
from pygame.locals import *
from pygame.mixer import Sound

class LcarsBackground(LcarsWidget):
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsBackgroundImage(LcarsWidget):
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
        LcarsWidget.__init__(self, None, (0,0), None)
    
    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.dirty = False        

    def handleEvent(self, event, clock):
        pass
    
class LcarsImage(LcarsWidget):
    def __init__(self, im, pos, handler=None):
        self.handler = handler
        image = pygame.image.load(im).convert()
        size = (image.get_rect().width, image.get_rect().height)
        print size
        self.image = image
        LcarsWidget.__init__(self, None, pos, size)

        #self.sound_beep1 = Sound("assets/audio/panel/206.wav")
        #self.sound_granted = Sound("assets/audio/accessing.wav")

    def handleEvent(self, event, clock):
        handled = False

        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            handled = True

        if (event.type == MOUSEBUTTONUP):
            if self.handler:
                self.handler(self, event, clock)
                handled = True

        LcarsWidget.handleEvent(self, event, clock)
        return handled
