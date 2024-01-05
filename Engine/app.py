import pygame
from sand_engine import space, display, world_camera
import sys

class App:
    def __init__(self, WIDTH=1000, HEIGHT=600):
        self.RES = WIDTH, HEIGHT
        pygame.init()
        self.screen = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()
        self.game = space.Space(4, 2)

        self.world_camera = world_camera.Camera()
        self.display = display.Display(self.game, self.world_camera)
        self.display.set_size(*self.RES, 4)

    def handle_events(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_z]:
            self.world_camera.zoom_in()
        if keys_pressed[pygame.K_x]:
            self.world_camera.zoom_out()

    def run(self):
        while True:
            self.handle_events()
            [self.exit() for event in pygame.event.get() if event.type == pygame.QUIT]

            self.screen.blit(self.display.get_surface(), (0,0))
            self.clock.tick()
            pygame.display.set_caption(f"Frame Rate: {int(self.clock.get_fps())} FPS")
            pygame.display.flip()


    def exit(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()
    