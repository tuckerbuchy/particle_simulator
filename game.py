import pygame
import random
import math
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
                                    x_vel=0,
                                    y_vel=0,
                                    m=random.randint(1, 10))
            particles.append(new_particle)

# TEACHME
# Why is this important. How can we tell when a particle is off the screen.
# Under what conditions does it fall off the screen.
def is_particle_off_screen(particle):
    if particle.x > width or \
            particle.x < 0 or \
            particle.y > height or \
            particle.y < 0:
        return True
    else:
        return False

# TEACHME
# Explain why we need to clean up particles. If we try to keep adding them what happens.
#
def cleanup_old_particles():
    for particle in particles:
        if is_particle_off_screen(particle):
            particles.remove(particle)

# TEACHME
# Explain how we calculate the distance between two points
#
def get_distance_between_points(x1, y1, x2, y2):
    x_distance = x2 - x1
    y_distance = y2 - y1

    distance = math.sqrt(x_distance**2 + y_distance**2)

    return distance

def get_gravitational_force_on_particle(particle1, particle2, r):
    """
    Calculates the gravitational force on two particles (p1, p2).

    This is based on the equation:

        F = g * (M1 * M2)/(r**2)

    https://en.wikipedia.org/wiki/Gravitational_acceleration

    :return: (absolute) force acting on particle1 and particle2
    """
    g = 0.125

    force = g * (particle1.mass * particle2.mass) / r**2

    return force


# TEACHME
# This is the hardest part of the whole application by far. All the math is locate
# in this function.
# Best to teach him all the other intricacies first.
def update_particles():
    for particle1 in particles:
        for particle2 in particles:
            if particle1 != particle2:

                x_diff = particle2.x - particle1.x
                y_diff = particle2.y - particle1.y

                distance = math.sqrt(x_diff**2 + y_diff**2)
                force = get_gravitational_force_on_particle(particle1, particle2, distance)

                # Force = Mass * Acceleration
                acceleration = force / particle1.mass

                particle1.x_velocity += acceleration * x_diff
                particle1.y_velocity += acceleration * y_diff

                particle1.x += particle1.x_velocity
                particle1.y += particle1.y_velocity

def draw_particles():
    for particle in particles:
        pygame.draw.circle(screen, colors.WHITE, (int(particle.x), int(particle.y)), particle.radius)

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

        # TEACHME
        # Explain how we can do this more effectively. Combine the two into one big 'update' loop.
        cleanup_old_particles()
        update_particles()
        draw_particles()

        draw_simulator_information()

        pygame.display.flip()


if __name__ == "__main__":
    start_game()