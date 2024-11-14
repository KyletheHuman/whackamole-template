import pygame

HEIGHT = 512
WIDTH = 640


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()



        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

            # Initialize game
            screen.fill("light green")
            draw_lines(screen)
            draw_mole(screen, mole_image, 0, 0)




            # Update the screen
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


def draw_lines(screen):
    # If the x value is divisible by 20, draw the line there
    j = 32
    for _ in range(20):
        pygame.draw.line(screen, "white", (j, 0), (j, HEIGHT))
        j += 32

    # If the y value is divisible by 16, draw the line there
    j = 32
    for _ in range(16):
        pygame.draw.line(screen, "white", (0, j), (WIDTH, j))
        j += 32

def draw_mole(screen, mole_image, x, y):
    screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))


if __name__ == "__main__":
    main()
