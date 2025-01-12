import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Define the vertices of the triangle
vertices = [
    (1, -1, -1),
    (-1, -1, -1),
    (0, 1, 0)
]

# Define the edges between the vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 0)
]

# Initialize the display
def init():
    glClearColor(0, 0, 0, 1)  # Set background color (black)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering

# Draw the triangle
def draw_triangle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Set up the OpenGL projection matrix
def setup_projection():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Main loop
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    init()
    setup_projection()

    # Main loop
    clock = pygame.time.Clock()
    angle = 0  # Rotation angle
    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer

        glPushMatrix()  # Save the current matrix
        glRotatef(angle, 1, 1, 0)  # Rotate around X and Y axes
        draw_triangle()
        glPopMatrix()  # Restore the matrix

        angle += 1  # Increment rotation angle

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

        # Exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()
