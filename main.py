import pygame
from board import Board

# GUI  Components

objects = []

class Button():
    def __init__(self, x, y, width, height, screen, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#914b00',
            'hover': '#6b3802',
            'pressed': '#914b00',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont(None, 40)
        self.buttonSurf = self.font.render(buttonText, True, (0, 0, 0))

        self.alreadyPressed = False

        self.screen = screen

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)


# Main Application

class App():
    def __init__(self):
        pygame.init()

        self.running = True
        
        self.title_font = pygame.font.SysFont(None, 48)
        self.screen = pygame.display.set_mode((1280, 720))
        self.title = pygame.display.set_caption("Chess by Luke")
        self.clock = pygame.time.Clock()

        self.BLACK = (0, 0, 0)

    def closeApp(self):
        self.running = False

    def run_bot_chess(self):
        print("Pressed Bot Chess")

    def run_online_chess(self):
        print("Pressed Online Chess")
  
    def setting_screen(self):
        title = self.title_font.render("CHESS", True, self.BLACK)

        self.screen.blit(title, (600, 50))

        playButton = Button(450, 250, 400, 100, self.screen, 'Play', self.run_bot_chess, True)
        onlineButton = Button(450, 400, 400, 100, self.screen, 'Online', self.run_online_chess, True)
        quitButton = Button(450, 550, 400, 100, self.screen, 'Quit', self.closeApp, True)
        
        playButton.process()
        onlineButton.process()
        quitButton.process()

    def game(self):
        pygame.display.flip()
        self.clock.tick() 
        self.screen.fill("white")

        self.setting_screen()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.game()
        pygame.quit();

if __name__ == "__main__":
    App().run()
