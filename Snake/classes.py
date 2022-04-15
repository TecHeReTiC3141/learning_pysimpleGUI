from constants import *
from collections import deque

directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}


class Apple:

    def __init__(self, x, y):
        self.x, self.y = x, y


class Snake:

    def __init__(self, segm: list[tuple], direction: str = 'right'):
        self.segm = deque(segm)
        self.head = segm[0]
        self.direction = direction

    def move(self):
        head, dirs = self.segm[0], \
                     directions[self.direction]
        self.segm.appendleft((head[0] + dirs[0],
                              head[1] + dirs[1]))
        self.head = self.segm[0]
        self.segm.pop()

    def set_dir(self, direct: str):
        self.direction = direct

    def draw_object(self) -> list:
        return [pos_to_pixel(*i) for i in self.segm]

    def collide(self, apples: list[Apple]):
        for apple in apples:
            if self.head[0] == apple.x and self.head[1] == apple.y:
                apples.remove(apple)
                tail = self.segm[-1]
                self.segm.append((tail[0] - directions[self.direction][0],
                                  tail[1] - directions[self.direction][1]))
