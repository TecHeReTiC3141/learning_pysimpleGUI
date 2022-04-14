from constants import *
from collections import deque

directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
class Snake:

    def __init__(self, segm: list[tuple], direction: str= 'right'):
        self.segm = deque(segm)
        self.direction = direction

    def move(self):
        head, dirs = self.segm[0], \
                     directions[self.direction]
        self.segm.appendleft((head[0] + dirs[0],
                              head[1] + dirs[1]))
        self.segm.pop()

    def set_dir(self, direct: str):
        self.direction = direct

    def draw_object(self):
        return [pos_to_pixel(*i) for i in self.segm]