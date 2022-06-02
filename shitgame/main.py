import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1280, 720
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
IMG_WIDTH, IMG_HEIGHT = 110, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tam liste")

WHITE = (255, 255, 255)
RED = (255,0,0)
BATU_JPG = pygame.image.load(os.path.join("assets", "batu.jpg"))
UMUT_JPG = pygame.image.load(os.path.join("assets", "umut.jpg"))
BACKGROUND_JPG = pygame.image.load(os.path.join("assets", "background.jpg"))

BATU = pygame.transform.scale(BATU_JPG, (IMG_WIDTH,IMG_HEIGHT))
UMUT = pygame.transform.scale(UMUT_JPG, (IMG_WIDTH,IMG_HEIGHT))
BACKGROUND = pygame.transform.scale(BACKGROUND_JPG, (WIDTH,HEIGHT))

BATU_HIT = pygame.USEREVENT + 1
FONT_HP = pygame.font.SysFont("comicsans", 40)
FONT_WINNER = pygame.font.SysFont("comicsans", 100)

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("assets", "bruh.wav"))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("assets", "hitsound.wav"))


def draw_window(batu, umut, umut_bullets, batu_hp):
	WIN.blit(BACKGROUND, (0,0))

	WIN.blit(BATU, (batu.x, batu.y))
	WIN.blit(UMUT, (umut.x, umut.y))

	hp_text = FONT_HP.render("HP : " + str(batu_hp), 1, RED)

	WIN.blit(hp_text, (WIDTH - hp_text.get_width(), 10))

	for bullet in umut_bullets:
		pygame.draw.rect(WIN, RED, bullet)

	pygame.display.update()

def draw_winner(text):
	draw_text = FONT_WINNER.render(text, 1, RED)
	WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width(), HEIGHT/2 - draw_text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(5000)

def batu_handle_movement(keys_pressed, batu):
	if (keys_pressed[pygame.K_a] and batu.x - VEL > 0): #left
		batu.x -= VEL
	if (keys_pressed[pygame.K_d] and batu.x + VEL < (WIDTH-IMG_WIDTH)): #right
		batu.x += VEL
	if (keys_pressed[pygame.K_w] and batu.y - VEL > 0): #up
		batu.y -= VEL
	if (keys_pressed[pygame.K_s] and batu.y + VEL < (HEIGHT-IMG_HEIGHT)): #down
		batu.y += VEL

def handle_bullets(umut_bullets, batu):
	for bullet in umut_bullets:
		bullet.x -= BULLET_VEL
		
		if bullet.x <= 0 or bullet.x >= WIDTH:
			umut_bullets.remove(bullet)
		
		if batu.colliderect(bullet):
			pygame.event.post(pygame.event.Event(BATU_HIT))
			umut_bullets.remove(bullet)

def main():
	batu = pygame.Rect(110, 100, IMG_WIDTH, IMG_HEIGHT)
	umut = pygame.Rect(700, 100, IMG_WIDTH, IMG_HEIGHT)

	BATU_HP = 100

	umut_bullets = []

	clock = pygame.time.Clock()

	run = True
	
	while (run):
		clock.tick(FPS)
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				run = False
				pygame.quit()
			
			if (event.type == pygame.KEYDOWN):
				if (event.key == pygame.K_SPACE):
					bullet = pygame.Rect(umut.x + umut.width/2, umut.y + umut.height / 2, 10, 5)
					umut_bullets.append(bullet)
					BULLET_FIRE_SOUND.play()

			if (event.type == BATU_HIT):
				BATU_HP -= 10
				BULLET_HIT_SOUND.play()
		
		if (BATU_HP <= 0):
			draw_winner("BATU DEAD")
			break

		keys_pressed = pygame.key.get_pressed()
		batu_handle_movement(keys_pressed, batu)
		draw_window(batu, umut, umut_bullets, BATU_HP)

		handle_bullets(umut_bullets, batu)
	
	main()

if __name__ == '__main__':
	main()
