import pygame

from settings import *
from road import draw_road
from traffic_light import TrafficLight
from vehicle import Vehicle

traffic_light = TrafficLight()
vehicles =[
    Vehicle(50,235),
    Vehicle(-80,235),
    Vehicle(-210,235),
    Vehicle(-340,235)
]

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

    for i, vehicle in enumerate(vehicles):

        vehicle_ahead = None

        if i > 0:
            vehicle_ahead = vehicles[i - 1]

        vehicle.update(
            traffic_light,
            STOP_LINE,
            vehicle_ahead
        )

    screen.fill(WHITE)
    
    draw_road(screen)
    
    traffic_light.draw(screen)

    for vehicle in vehicles:
        vehicle.draw(screen)

    pygame.display.flip()

pygame.quit()