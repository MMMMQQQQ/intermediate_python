import pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS=10
STARTING_RED_BLOBS=3

WIDTH=800
HEIGHT=600
# RGB
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)

game_display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock=pygame.time.Clock()

class BlueBlob(Blob):
    def __init__(self,color,x_boundary,y_boundary):
        super().__init__(color,x_boundary,y_boundary)
        # Blob.__init__(self,color, x_boundary, y_boundary)
        self.color=BLUE

    def move_faster(self):
        self.x+=random.randrange(-7,7)
        self.y += random.randrange(-7, 7)


def draw_environment(blue_list):
    # this is used to redraw the frame every time the frame is reloaded
    game_display.fill(WHITE)
    for blob_dict in blue_list:
        for blob_id in blob_dict:
            blob=blob_dict[blob_id]

    # this line is after the fill
            pygame.draw.circle(game_display,blob.color,[blob.x,blob.y],blob.size)

            blob.move_faster()
            blob.check_bounds()
    pygame.display.update()



def main():
    # red_blob=Blob(RED)
    # we will create a bunch of blobs
    blue_blobs=dict(enumerate([BlueBlob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS) ]))
    red_blobs = dict(enumerate([BlueBlob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs,red_blobs])
        clock.tick(60)
        # print(blue_blobs.x,blue_blobs.y)

if __name__=='__main__':
    main()