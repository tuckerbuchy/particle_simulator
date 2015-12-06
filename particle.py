class Particle:
    """
    A class used to model a particle in the simulator.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, m):
        # What is needed in a particle?
        self.x_position = x_pos
        self.y_position = y_pos

        self.x_velocity = x_vel
        self.y_velocity = y_vel

        self.mass = m

        self.radius = self.mass