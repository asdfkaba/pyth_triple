from __future__ import division
import random
from PIL import Image, ImageFont, ImageDraw

def draw(size, res, x, y, z):
    scale=size
    draw_y = (y/z) * scale
    draw_x = (x/z) * scale
    scale_factor = scale/z

    im = Image.new('RGB', (scale,scale), (255,0,0))
    dr = ImageDraw.Draw(im)
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', int(scale/25))

    def get_color():
        levels = range(32,256,32)
        return tuple(random.choice(levels) for _ in range(3))

    # draw y^2
    dr.rectangle(((0,scale),(draw_y,scale-draw_y)), fill='brown' , outline='black')

    # draw rectlinear polygon in top right corner
    dr.rectangle(((scale-draw_x,scale-draw_y),(scale,0)), fill="green")
    dr.rectangle(((scale-(scale-draw_y),0),(scale,draw_x)), fill="green")

    # draw splitted pieces
    up_start = (0,0)
    down_start = (draw_y,draw_x)
    square_start = (scale-draw_x,scale-draw_y)
    count = 0
    old = None
    col_finished = False
    for i in range(2,len(res)):
        height = scale_factor*res[i].height
        width = scale_factor*res[i].width
        long_site = height if height > width else width
        short_site = width if height > width else height
        color = get_color()

        # draw top left corner if anything left to draw there
        if i % 2 == 0 and count < (z-x)*(z-y):
            dr.rectangle(((up_start[0], up_start[1]),(up_start[0]+long_site, up_start[1]+short_site)),  fill=color, outline='white')

            # calc next (x,y) to start drawing in bottom right corner
            if 1 + up_start[0] + long_site < (scale-draw_x):
                up_start = (up_start[0] + long_site, up_start[1] + 0)
            else:
                up_start = (up_start[0], up_start[1] + short_site)
            count += res[i].width*res[i].height
        # draw bottom right corner
        else:
            potrait = not abs(down_start[1]+short_site-scale) < 1 and not abs(down_start[0]+long_site-scale) < 1
            dr.rectangle(((down_start[0],down_start[1]),(down_start[0] + (short_site if potrait else long_site), down_start[1] + (long_site if potrait else short_site))), fill=color,  outline='white')

            # calc next (x,y) to start drawing in bottom right corner
            if (1 + down_start[1] + (long_site if potrait else short_site)) < (scale):
               down_start = (down_start[0], down_start[1] + (long_site if potrait else short_site))
            else:
               down_start = (down_start[0] + (short_site if potrait else long_site), down_start[1])

        # draw in square
        if old is not None and (col_finished or square_start[1]+height > draw_x):
            square_start = old
            old = None
        elif abs(square_start[0] + width - draw_y) > 2  and abs(square_start[1] + height - draw_x) > 2:
            old = (square_start[0] + width, square_start[1])

        dr.rectangle(((square_start[0],square_start[1]),(square_start[0]+ width, square_start[1]+ height)), fill=color, outline='white')

        col_finished = True if abs(square_start[1] + height - draw_x) < 1 else False


        # calc next (x,y) to start drawing in square
        if abs(square_start[0] + width - draw_y) < 2:
            square_start = (square_start[0], square_start[1] + height)
        elif abs(square_start[0] + width - draw_y) > 2 and abs(square_start[1] + height - draw_x) > 2:
            square_start = (square_start[0], square_start[1] + height)
        else:
            square_start = (square_start[0] + width , square_start[1])


    dr.text((int(scale/8),scale-int(scale/4)), str(x)+"^2 + " +str(y) + "^2 = "+str(z)+"^2", font=fnt, fill=(255,255,255,128))
    dr.text((int(scale/8),scale-int(scale/6)), "pieces: "+str(len(res)), font=fnt, fill=(255,255,255,128))

    dr.rectangle(((0,scale),(draw_y,scale-draw_y)), outline='black')
    dr.rectangle(((scale-draw_x,0),(scale,draw_x)), outline='yellow')
    dr.rectangle(((0,0),(scale,scale)), outline='black')

    im.save(str(x)+"_"+str(y)+"_"+str(z)+"_triple.png")
