import pygame

from settings import *
from road import draw_road
from traffic_light import TrafficLight
from vehicle import Vehicle

traffic_light = TrafficLight()
car = Vehicle(50, 235)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Light Simulation")

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    traffic_light.update()

    car.update(traffic_light, STOP_LINE)

    screen.fill(WHITE)
    
    draw_road(screen)
    
    traffic_light.draw(screen)

    car.draw(screen)

    pygame.display.flip()

pygame.quit()