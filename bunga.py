import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Lebar dan tinggi layar
width, height = 400, 400

# Ukuran blok
block_size = 20

# Membuat layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Obstacle Snake")

# Fungsi utama
def main():
    running = True
    clock = pygame.time.Clock()
    
    snake = [(width // 2, height // 2)]
    food = spawn_food(snake)
    direction = (1, 0)
    
    # Inisialisasi rintangan
    obstacles = []
    for _ in range(10):
        obstacles.append(spawn_obstacle(snake + obstacles))
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
        if keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
        if keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
        if keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)
        
        new_head = (snake[0][0] + direction[0] * block_size, snake[0][1] + direction[1] * block_size)
        snake.insert(0, new_head)
        
        if snake[0] == food:
            food = spawn_food(snake)
        else:
            snake.pop()
        
        # Cek tabrakan dengan rintangan
        if snake[0] in obstacles:
            running = False
        
        # Menggambar elemen-elemen permainan
        screen.fill(white)
        for segment in snake:
            pygame.draw.rect(screen, green, (segment[0], segment[1], block_size, block_size))
        pygame.draw.rect(screen, green, (food[0], food[1], block_size, block_size))
        for obstacle in obstacles:
            pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], block_size, block_size))
        
        pygame.display.flip()
        clock.tick(10)  # Kecepatan ular bergerak
        
    pygame.quit()

def spawn_food(snake):
    while True:
        food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
        if food not in snake:
            return food

def spawn_obstacle(exclude_positions):
    while True:
        obstacle = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
        if obstacle not in exclude_positions:
            return obstacle

if __name__ == "__main__":
    main()
