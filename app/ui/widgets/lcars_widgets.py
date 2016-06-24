import pygame
from pygame.font import Font
from pygame.locals import *
from pygame.mixer import Sound

from ui.widgets.sprite import LcarsWidget
from ui import colours


class LcarsElbow(LcarsWidget):
    """The LCARS corner elbow - not currently used"""
    
    #STYLE_BOTTOM_LEFT = 0
    #STYLE_TOP_LEFT = 1
    #STYLE_BOTTOM_RIGHT = 2
    #STYLE_TOP_RIGHT = 3
    
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/elbow.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - 219,
                    image.get_rect().height - textImage.get_rect().height - 35))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled

class LcarsTab(LcarsWidget):
    STYLE_LEFT = 1
    STYLE_RIGHT = 2
    
    def __init__(self, colour, style, pos):
        image = pygame.image.load("assets/tab.png").convert()
        if (style == LcarsTab.STYLE_RIGHT):
            image = pygame.transform.flip(image, False, True)
        
        size = (image.get_rect().width, image.get_rect().height)
        LcarsWidget.__init__(self, colour, pos, size)
        self.image = image
        self.applyColour(colour)

class LcarsButton(LcarsWidget):
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/button.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled

class LcarsImageButton(LcarsWidget):
    def __init__(self, image, pos, handler=None):
        self.handler = handler

        self.image = pygame.image.load(image).convert()
        LcarsWidget.__init__(self, None, pos, None)

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
            
    
class LcarsText(LcarsWidget):
    def __init__(self, colour, pos, message, size=1.0, background=None):
        self.colour = colour
        self.background = background
        self.font = Font("assets/swiss911.ttf", int(19.0 * size))
        
        self.renderText(message)
        # center the text if needed 
        if (pos[1] < 0):
            pos = (pos[0], 400 - self.image.get_rect().width / 2)
            
        LcarsWidget.__init__(self, colour, pos, None)

    def renderText(self, message):        
        if (self.background == None):
            self.image = self.font.render(message, True, self.colour)
        else:
            self.image = self.font.render(message, True, self.colour, self.background)
        
    def setText(self, newText):
        self.renderText(newText)

class LcarsBlockHuge(LcarsWidget):
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/hugeRectangle.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled

class LcarsBlockLarge(LcarsWidget):
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/largeRectangle.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled

class LcarsBlockSmall(LcarsWidget):
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/smallRectangle.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - textImage.get_rect().width - 10,
                    image.get_rect().height - textImage.get_rect().height - 5))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled
        

        
class LcarsTabBlock(LcarsWidget):
    def __init__(self, colour, pos, text, handler=None):
        self.handler = handler
        image = pygame.image.load("assets/tab.png").convert()
        size = (image.get_rect().width, image.get_rect().height)
        font = Font("assets/swiss911.ttf", 19)
        textImage = font.render(text, False, colours.BLACK)
        image.blit(textImage, 
                   (image.get_rect().width - 135,
                    image.get_rect().height - textImage.get_rect().height - 10))

        self.image = image
        self.colour = colour
        LcarsWidget.__init__(self, colour, pos, size)
        self.applyColour(colour)
        self.highlighted = False
        self.beep = Sound("assets/audio/panel/202.wav")

    def handleEvent(self, event, clock):
        handled = False
        
        if (event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)):
            self.applyColour(colours.WHITE)
            self.highlighted = True
            self.beep.play()
            handled = True

        if (event.type == MOUSEBUTTONUP and self.highlighted):
            self.applyColour(self.colour)
            if self.handler:
                self.handler(self, event, clock)
                handled = True
            
        LcarsWidget.handleEvent(self, event, clock)
        return handled     
        
