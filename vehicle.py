import pygame

class Vehicle:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

        self.width = 60
        self.height = 30 

        self.speed = 3

    def update(self, traffic_light, stop_line, vehicle_ahead=None):
        if vehicle_ahead:
            safe_distance = 20

            if (vehicle_ahead.x - (self.x + self.width)) < safe_distance:
                return
        
        if traffic_light.state == "RED":
            if self.x + self.width < stop_line:
                self.x += self.speed
        
        else: 
            self.x += self.speed
    
    def draw(self, screen):

        pygame.draw.rect(screen, (0,100,255), (self.x, self.y, self.width, self.height))
