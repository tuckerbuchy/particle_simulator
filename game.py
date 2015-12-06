import pygame
import random
import colors
from particle import Particle

pygame.init()

# Set the Screen width
width = 800
# Set the Screen height
height = 600

# Set up the display window
screen = pygame.display.set_mode((width, height))

# A place to store the particles in the game.
particles = []

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            new_particle = Particle(x_pos=mouse_x,
                                    y_pos=mouse_y,
                                    x_vel=random.randint(-10, 10),
                                    y_vel=random.randint(-10, 10),
                                    m=random.randint(1, 10))
            particles.append(new_particle)

# TEACH
# Why is this important. How can we tell when a particle is off the screen.
# Under what conditions does it fall off the screen.
def is_particle_off_screen(particle):
    if particle.x_position > width or \
            particle.x_position < 0 or \
            particle.y_position > height or \
            particle.y_position < 0:
        return True
    else:
        return False

# TEACH
# Explain why we need to clean up particles. If we try to keep adding them what happens.
#
def cleanup_old_particles():
    for particle in particles:
        if is_particle_off_screen(particle):
            particles.remove(particle)


def update_particles():
    for particle in particles:
        particle.x_position += particle.x_velocity
        particle.y_position += particle.y_velocity
        pygame.draw.circle(screen, colors.WHITE, (particle.x_position,particle.y_position), particle.radius)

def draw_simulator_information():
    font = pygame.font.SysFont('verdana', 12)

    number_of_particles = len(particles)
    text = "Particles: {}".format(number_of_particles)

    text_box = font.render(text, True, (0, 255, 0))
    screen.blit(text_box, (0,0))

def start_game():

    # The main game loop.
    while True:
        screen.fill(colors.BLACK)
        handle_events()

        # TEACH
        # Explain how we can do this more effectively. Combine the two into one big 'update' loop.
        cleanup_old_particles()
        update_particles()

        draw_simulator_information()

        pygame.display.flip()


if __name__ == "__main__":
    start_game()