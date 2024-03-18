import pygame
import random

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

def Simulate(ParticlePositionsIn, container_rect, shrink_rate, elapsed_time):
    ParticlePositions = ParticlePositionsIn
    
    # Simulate particle movement (ideal gas-like behavior)
    for particle in ParticlePositions:
        dx = random.uniform(-1, 1)
        dy = random.uniform(-1, 1)
        new_x = particle[0] + dx
        new_y = particle[1] + dy

        # Keep particles within the container rectangle
        new_x = max(container_rect.left, min(new_x, container_rect.right))
        new_y = max(container_rect.top, min(new_y, container_rect.bottom))

        particle[0] = new_x
        particle[1] = new_y

    # Shrink the container rectangle based on elapsed time
    container_rect.inflate_ip(-shrink_rate * elapsed_time, -shrink_rate * elapsed_time)

    return ParticlePositions

def ColorParticlesByPressure(pressure):
    # Map pressure to color (warmer colors for higher pressure)
    min_pressure = 90000  # Adjust as needed
    max_pressure = 110000  # Adjust as needed
    normalized_pressure = (pressure - min_pressure) / (max_pressure - min_pressure)
    red = int(255 * normalized_pressure)
    blue = int(255 * (1 - normalized_pressure))
    return red, 0, blue

def DrawParticles(ParticlePositions):
    for Particle in ParticlePositions:
        pressure = random.uniform(90000, 110000)  # Simulated pressure (adjust as needed)
        color = ColorParticlesByPressure(pressure)
        pygame.draw.circle(screen, color, (int(Particle[0]), int(Particle[1])), 2)
        
def StartSimulation(Particles):
    ParticlePositionsOut = []
    for _ in range(Particles):
        x = random.randint(350, 600)
        y = random.randint(300, 750)
        ParticlePositionsOut.append([x, y])
    return ParticlePositionsOut

# Define the initial container rectangle
container_rect = pygame.Rect(350, 300, 250, 450)
shrink_rate = 0  # Adjust as needed

ParticlePositions = StartSimulation(1000)

start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightblue")
    pygame.draw.rect(screen, "white", container_rect)

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000.0  # Convert to seconds

    # Simulate particle movement and shrink the container
    ParticlePositions = Simulate(ParticlePositions, container_rect, shrink_rate, elapsed_time)

    # Draw particles with pressure-based colors
    DrawParticles(ParticlePositions)

    pygame.display.flip()
    clock.tick(1000)  # Limits FPS to 10

pygame.quit()
