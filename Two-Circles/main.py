"""App that shows the state of two circles"""
import sys

import pygame


def get_inputs():
    """Get radii and distance between circles"""
    radius1 = int(input("Enter the radius of the first circle: "))
    radius2 = int(input("Enter the radius of the second circle: "))
    distance = int(input("Enter the distance between the two circles: "))

    return (radius1, radius2, distance)


def identify_circles(radius1, radius2):
    """Returns which circle is bigger and which is smaller"""
    if radius1 > radius2:
        bigger, smaller = radius1, radius2
    else:
        bigger, smaller = radius2, radius1

    return (bigger, smaller)


def get_state(bigger, smaller, distance):
    """Identifies the state of the two circles"""
    edge_distance = distance - bigger - smaller

    if distance == 0:
        if bigger == smaller:
            return "The circles are the same"
        return "The circles are concentric"

    if edge_distance in (0, -2 * smaller):
        return "The circles have one point of intersection"

    if edge_distance > 0 or edge_distance < -2 * smaller:
        return "The circles have no points of intersection"

    return "The circles have two points of intersection"


def draw_circles(bigger, smaller, distance, state):
    """Draws the circles to the pygame display"""
    centre1 = 100 + bigger
    centre2 = centre1 + distance
    y_pos = 50 + bigger

    pygame.draw.circle(SCREEN, (255, 0, 0), (centre1, y_pos), bigger, 1)
    pygame.draw.circle(SCREEN, (0, 255, 0), (centre2, y_pos), smaller, 1)

    state_font = pygame.font.SysFont("Helvetica", 18)
    textsurface = state_font.render(state, False, (0, 0, 0))
    SCREEN.blit(textsurface, (WIDTH / 2 - textsurface.get_width() / 2, HEIGHT - 35))


if __name__ == "__main__":
    radius1, radius2, distance = get_inputs()
    bigger, smaller = identify_circles(radius1, radius2)

    scale_factor = int(50 / bigger)
    bigger *= scale_factor
    smaller *= scale_factor
    distance *= scale_factor

    pygame.init()
    pygame.font.init()

    if smaller + distance > bigger:
        WIDTH = 100 + 2 * (bigger + smaller) + distance
    else:
        WIDTH = 200 + 2 * bigger

    HEIGHT = 200

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    SCREEN.fill((255, 255, 255))
    pygame.display.set_caption("State of two circles")

    state = get_state(bigger, smaller, distance)
    draw_circles(bigger, smaller, distance, state)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        pygame.display.update()
