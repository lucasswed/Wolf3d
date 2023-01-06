import pygame
import sys
import os

def read_files():
	pasta = '../wolf3D_py'
	for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))

def main():
	map = read_map()
	pygame.init()
	pygame.display.init()
	screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)# | pygame.FULLSCREEN)
	while True:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			screen.fill((0, 0, 0))
			pygame.display.flip()


if __name__ == "__main__":
	main()