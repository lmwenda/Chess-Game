import pygame
from Button import Button
from board import Board

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

    def setting_screen(self):
        title = self.title_font.render("CHESS", True, self.BLACK)

        self.screen.blit(title, (600, 50))

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
