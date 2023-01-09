import pygame
import sys
import os

def read_files():
	maps = []
	pasta = 'C:\\Users\\User\\Desktop\\Wolf3d'
	for diretorio, subpastas, arquivos in os.walk(pasta):
		for arquivo in arquivos:
			if ".cub" in arquivo:
				maps.append(os.path.join(diretorio, arquivo))
	return maps


def read_map(map_file):
	map = []
	with open(map_file, 'r') as fd:
		for line in fd:
			map.append(line.strip())
	print(map)
	return map


def get_user_input(map_list):
	len = 0
	for count, line in enumerate(map_list):
		print(count, line)
		len = len + 1
	user_input = input("Escreva o numero correspondente ao mapa que quer jogar: ").strip()
	if not user_input.isdigit():
			user_input = -1
	user_input = int(user_input)
	while user_input >= len or user_input < 0:
		user_input = input("Escreva o numero correspondente ao mapa que quer jogar: ").strip()
		if not user_input.isdigit():
			user_input = -1
		user_input = int(user_input)
	return user_input

def main(screenx=1920, screeny=1080):
	map_list = read_files()
	i = get_user_input(map_list)
	read_map(map_list[i])
	pygame.init()
	pygame.display.init()
	screen = pygame.display.set_mode((screenx, screeny), pygame.RESIZABLE | pygame.SCALED)# | pygame.FULLSCREEN)
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
	screenx = 1080
	screeny = 720
	main(screenx, screeny)