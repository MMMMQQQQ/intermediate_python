import pygame
import random
from blob import Blob
import numpy as np
import logging

'''
DEBUG Detailed information, typically of interest only when diagnosing problems
INFO  Confirmation that things are working as expected
WARNING  An indication that something unexpected happened, or indicative of some problem in the ne
ERROR   DUE to a more serious problem, the software has not been able to perform some function
CRITICAL  A serious error, indicating that the problem itself may be unable to continue to run
'''

logging.basicConfig(filename='logfile.txt', level=logging.INFO)

STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15

WIDTH = 800
HEIGHT = 600
# RGB
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        logging.info('Blob add op {}+{}'.format(str(self), str(other_blob)))
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size

        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0

        elif other_blob.color == (0, 0, 255):
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of imsupported colors.')


class RedBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)


def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)


def handle_collision(blob_list):
    # unpack the list
    blues, reds, greens = blob_list
    #     bacause the blob list is the dictionary, and we do not wanto to modify the original one
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug(
                    'Checking if blobs are touching {}+{}'.format(str(blue_blob), str(other_blob)))
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        elif blue_blob.size <= 0:
                            del blues[blue_id]
    return blues, reds, greens


def draw_environment(blob_list):
    blues, reds, greens = handle_collision(blob_list)
    # this is used to redraw the frame every time the frame is reloaded
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]

            # this line is after the fill
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)

            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds, greens


def main():
    # red_blob=Blob(RED)
    # we will create a bunch of blobs
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

    # print('Blue blob size: {}, Red blob size: {}'.format(blue_blobs[0].size,red_blobs[0].size))
    # blue_blobs[0]+red_blobs[0]
    # print('Blue blob size: {}, Red blob size: {}'.format(blue_blobs[0].size, red_blobs[0].size))

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            blues, reds, greens = draw_environment([blue_blobs, red_blobs, green_blobs])
            clock.tick(60)
            # print(blue_blobs.x,blue_blobs.y)
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break


if __name__ == '__main__':
    # blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    # red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    # green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    # pygame.quit()
    #
    main()