import pygame
import asyncio

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Test")

font = pygame.font.Font(None, 50)
user_text = ""

async def main():
    global user_text
    running = True
    while running:
        screen.fill((30, 30, 30))  # Dark background
        text_surface = font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (20, HEIGHT // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    user_text = ""
                else:
                    user_text += event.unicode

        await asyncio.sleep(0)  # Prevents freezing in the browser

asyncio.run(main())  # Run async loop
pygame.quit()
