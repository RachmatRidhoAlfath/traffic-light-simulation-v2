import pygame
import time

class TrafficLight:
    def __init__(self):
        
        self.state = "RED"
        self.red_time = 5
        self.yellow_time = 2
        self.green_time = 5

        self.last_change = time.time()

    def update(self):
        elapsed = time.time() - self.last_change

        if self.state == "RED" and elapsed >= self.red_time:
            self.state = "GREEN"
            self.last_change = time.time()

        elif self.state == "GREEN" and elapsed >= self.green_time:
            self.state = "YELLOW"
            self.last_change = time.time()

        elif self.state == "YELLOW" and elapsed >= self.yellow_time:
            self.state = "RED"
            self.last_change = time.time()

    def draw(self, screen):
        pygame.draw.rect(screen, (40,40,40), (850,100,60,180))

        red = (255,0,0) if self.state == "RED" else (100,100,100)
        yellow = (255,255,0) if self.state == "YELLOW" else (100,100,100)
        green = (0,255,0) if self.state == "GREEN" else (100,100,100)

        pygame.draw.circle(screen, red, (880, 130), 20)
        pygame.draw.circle(screen, yellow, (880,190), 20)
        pygame.draw.circle(screen, green, (880, 250), 20)
