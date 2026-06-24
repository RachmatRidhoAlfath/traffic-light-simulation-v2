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

spawn_timer = 0
spawn_delay = 180

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    traffic_light.update()
    spawn_timer += 1

    if spawn_timer >= spawn_delay:

        vehicles.append(
            Vehicle(-100, 235)
        )

        spawn_timer = 0

    for i, vehicle in enumerate(vehicles):

        vehicle_ahead = None

        if i > 0:
            vehicle_ahead = vehicles[i - 1]

        vehicle.update(
            traffic_light,
            STOP_LINE,
            vehicle_ahead
        )

    vehicles = [
        car for car in vehicles
        if car.x < WIDTH + 100
    ]   
    screen.fill(WHITE)
    
    draw_road(screen)
    
    traffic_light.draw(screen)

    for vehicle in vehicles:
        vehicle.draw(screen)

    pygame.display.flip()

pygame.quit()