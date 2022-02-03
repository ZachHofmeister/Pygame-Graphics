import pygame as pg
import sys
from pygame.locals import *
from math import sqrt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# YOUR CODE HERE  ...


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from(self, other):
        delx = self.x - other.x
        dely = self.y - other.y
        return sqrt(delx ** 2 + dely ** 2)

    @staticmethod
    def run_tests():
        print()
        p = Point()
        p2 = Point(x=3, y=-4)
        print(f'p is {p}')
        print(f'p2 is {p2}')
        print(f'{p} is {p.distance_from(p2)} from {p2}')


class Circle:
    def __init__(self, radius, center=Point(), color=RED):
        self.radius = radius
        self.center = center
        self.color = color

    def __str__(self):
        return f'[Circle, r={self.radius :2}, ctr={self.center}, area={self.area() :6.2f}, peri={self.peri() :6.2f}]'

    def area(self): return 3.14159 * self.radius ** 2

    def peri(self): return 3.14159 * 2 * self.radius

    def move_to(self, point):
        self.center.x = point.x
        self.center.y = point.y

    def move_by(self, point):
        self.center.x += point.x
        self.center.y += point.y

    def update(self):
        # if touch_bottom or touch_top: self.v.y *= -1
        # if touch_left or touch_right: self.v.x *= -1
        # r, x, y = self.radius, self.center.x, self.center.y
        # if y + r < 0 || y + r > self.height: self.v.y *= -1
        # if x + r < 0 || x + r > self.width: self.v.x *= -1

        pass

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.center.x, self.center.y), self.radius, 0)


    @staticmethod
    def run_tests():
        print()
        c = Circle(radius=5)
        c2 = Circle(radius=10, center=Point(99, 99))
        print(f' c is {c}')
        print(f'c2 is {c2}')

        c.move_to(Point(5, 9))
        c2.move_by(Point(-1, -1))
        print('after moving...')
        print(f' c is {c}')
        print(f'c2 is {c2}')


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500, 400), 0, 32)
        pg.display.set_caption('Python Graphics App')
        self.basic_font = pg.font.SysFont(None, 48)
        # self.circle1 = Circle(radius=40, center=Point(x=460, y=60))
        # self.circle2 = Circle(radius=20, center=Point(x=300, y=250))

    def __repr__(self):
        return f'Polygon Graphics Game'

    def play(self):
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            self.draw()
            self.update()

            for event in pg.event.get():
                if event.type == QUIT:
                    finished = True

        pg.quit()  # game finished
        sys.exit()

    def draw(self):
        self.draw_circles()
        self.draw_polygons()
        self.draw_lines()
        self.draw_text()

    def update(self):
        pg.display.update()

    def draw_lines(self):
        pg.draw.line(self.screen, BLUE, (60, 60), (120, 60), 4)
        pg.draw.line(self.screen, BLUE, (120, 60), (60, 120))
        pg.draw.line(self.screen, BLUE, (60, 120), (120, 120), 4)

    def update_circles(self):
        pass

    def draw_circles(self):
        pg.draw.circle(self.screen, BLUE, (300, 50), 20, 0)
        pg.draw.ellipse(self.screen, RED, (300, 250, 40, 80), 1)

    def draw_polygons(self):
        pg.draw.polygon(self.screen, GREEN, ((146, 0), (291, 106),
                                        (236, 277), (56, 277), (0, 106)))

    def draw_text(self):
        text = self.basic_font.render('Hello world!', True, WHITE, BLUE)

        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery

        pg.draw.rect(self.screen, RED, (text_rect.left - 20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

        pix_array = pg.PixelArray(self.screen)
        pix_array[480][380] = BLACK
        del pix_array

        self.screen.blit(text, text_rect)


# END YOUR CODE


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()