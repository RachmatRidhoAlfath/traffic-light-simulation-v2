import pygame
import random

class Vehicle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        vehicle_types = [
            (60, 30),   # mobil kecil
            (80, 35),   # mobil sedang
            (100, 40)   # bus/truk
        ]

        self.width, self.height = random.choice(vehicle_types)

        self.speed = 3


        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def update(self, traffic_light, stop_line, vehicle_ahead=None):

        front_of_car = self.x + self.width

    # Jika sudah melewati garis stop, terus jalan
        if front_of_car >= stop_line:
            self.x += self.speed
            return

    # Jaga jarak dengan kendaraan depan
        if vehicle_ahead:

            safe_distance = 20

            distance = vehicle_ahead.x - front_of_car

            if distance < safe_distance:
                return

    # Hanya berhenti saat lampu merah
        if traffic_light.state == "RED":

            next_front = front_of_car + self.speed

            if next_front >= stop_line:
                return

    # Lampu hijau dan kuning tetap jalan
        self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )