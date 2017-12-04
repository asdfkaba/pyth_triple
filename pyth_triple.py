from __future__ import print_function
from __future__ import division
import argparse
import sys
import itertools
from PIL import Image, ImageFont, ImageDraw


parser = argparse.ArgumentParser(description='Calculate minimal partition for pythagorean triple')
parser.add_argument('x', metavar='x', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')
parser.add_argument('y', metavar='y', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')
parser.add_argument('z', metavar='z', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')

args = parser.parse_args()

class Triple:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
         return '('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'

class Rect:
    def __init__(self, picture, width, height):
        self.picture = picture
        self.width = width
        self.height = height

    def __str__(self):
        if self.picture.startswith('B'):
            return self.picture
        return self.picture+' (width: '+str(self.width)+', height: '+str(self.height)+')'

    def __repr(self):
        return str(self)

def is_finished(rects, val):
    # is sum(area(rect)) correct?
    tmp = 0
    for rect in rects:
            print(rect)
            tmp+=rect.width*rect.height
    print(str(val) + 'vs' + str(tmp))
    return val==tmp

def build_split_up(rest_of_c, rest_of_d):

    solution = []
    x,y = rest_of_d.width, rest_of_d.height
    second = rest_of_c
    i = 0
    while(not is_finished(solution, x*y)):
        if i > 6:
            break
        if i < 3:
            print('##')
            print(rest_of_c)
            print(second)
            print(rest_of_d)
            print('##')
        i += 1
        if rest_of_c.width<rest_of_d.width and second.width<rest_of_d.width:
            print(1, end='')
            candidate_width= rest_of_c.width
            second_width= second.width
            if rest_of_c.height + second.height < rest_of_d.height:
                print(1, end='')
                candidate_height = rest_of_c.height
                second_height = second.height
                rest_of_d= Rect('dummy', rest_of_d.width, rest_of_d.height-rest_of_c.height)
            else:
                print(2, end='')
                candidate_height = rest_of_c.height
                second_height = rest_of_d.height-candidate_height
                rest_of_d= Rect('dummy', rest_of_d.width-candidate_width, rest_of_d.height)
            rest_of_c= Rect('dummy', rest_of_c.width, rest_of_c.height-candidate_height)
            second= Rect('dummy', second.width, second.height-second_height)
        else:
            print(2, end='')
            if rest_of_c.height + second.height < rest_of_d.height:
                print(1, end='')
                candidate_height = rest_of_c.height
                second_height = second.height
            else:
                print(2, end='')
                candidate_height = rest_of_c.height
                second_height = rest_of_d.height-candidate_height
            candidate_width = rest_of_d.width
            second_width = rest_of_d.width
            rest_of_d= Rect('', rest_of_d.width, rest_of_d.height-rest_of_c.height-second.height)
            rest_of_c= Rect('', rest_of_c.width-candidate_width, rest_of_c.height)
            second= Rect('', second.width-candidate_width, second.height)
        print('')
        candidate = Rect('Part of D from splitted Cs in Picture', candidate_width, candidate_height)
        second_candidate = Rect('Part of D from splitted Cs in Picture', second_width, second_height)
        if candidate.width > 0 and candidate.height > 0:
            solution.append(candidate)
        if second_candidate.width > 0 and second_candidate.height > 0:
            solution.append(second_candidate)
    return solution


def calc(triple):
    solution = []
    # append square with area=y^2 (PICTURE: A)
    solution.append(Rect('A in Picture', triple.y, triple.y))
    # append rect angle form (PICTURE: B)
    solution.append(Rect('B in Picture', triple.x, triple.z-triple.y))

    # missing pieces(2 equal forms with width m=z-x and height n=z-y (PICTURE: C)) which we have to split up to fill rest_of_d.size n^2 with n = x-(z-y))
    # together with rect angle form with minimal possible amount of pieces
    c = Rect('dummy', triple.z-triple.x, triple.z-triple.y)
    d_length = triple.x-(triple.z-triple.y)
    d = Rect('dummy', d_length, d_length)

    # do the minimal split up and append result to solution
    solution += build_split_up(c, d)

    return solution


x,y,z = vars(args).get('x')[0], vars(args).get('y')[0], vars(args).get('z')[0]
if pow(x,2) + pow(y,2) != pow(z, 2):
    print("x,y,z is not a pythagorean triple")
    sys.exit(0)
trip = Triple(x if x < y else y ,y if x < y else x,z)
res = calc(trip)

print("##########################")
print("# x="+str(x)+", y="+str(y)+", z="+str(z))
print("# x^2 + y^2 = z^2")
print("# _________________")
print("# |  C   |         |")
print("# |______|______ B |")
print("# |            |   |")
print("# |            |   |")
print("# |     A      |___|")
print("# |            |   |")
print("# |            | C |")
print("# |____________|___|")
print("#")
print("#  area(complete square = z^2 = " + str(pow(z,2)))
print("#  area(A) = y^2 = " + str(pow(y,2)))
print("#  length_out(B) = x = " +str(x))
print("#  length_inner(B) = x-(z-y) = " +str(x-(z-y)))
print("#  area(C) = z-x*z-y = "+str(z-x)+"*"+str(z-y)+" = "+str((z-x)*(z-y)))
print("#")
print("# square with size x^2 " + "square with size y^2")
print("# _________________ " + "   " + "_________________")
print("# |                |" + "   " + "|                |")
print("# |____________  B |" + "   " + "|                |")
print("# |            |   |" + "   " + "|                |")
print("# |            |   |" + "   " + "|       A        |")
print("# |     D      |   |" + "   " + "|                |")
print("# |            |   |" + "   " + "|                |")
print("# |            |   |" + "   " + "|                |")
print("# |____________|___|" + "   " + "|________________|")
print("#")
print("# Build D out of 2 Cs with minimum splitups")
print("# D needs to be: "+str(x-(z-y))+"*"+str(x-(z-y)))
print("# C is: "+str(z-x)+"*"+str(z-y))
print("#")
print("##########################")
print("Result Parts:")
for re in res:
    print(str(re))


scale=1000
draw_y = (y/z) * scale
draw_x = (x/z) * scale

real_scale = scale/z

im = Image.new('RGB', (scale,scale), (255,0,0))
dr = ImageDraw.Draw(im)
fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)


dr.rectangle(((0,scale),(draw_y,scale-draw_y)), fill="brown", outline='black')

dr.rectangle(((scale-draw_x,scale-draw_y),(scale,0)), fill="green")
dr.rectangle(((scale-(scale-draw_y),0),(scale,draw_x)), fill="green")

# draw splitted pieces
up_start = (0,0)
down_start = (draw_y,draw_x)
square_start = (scale-draw_x,scale-draw_y)
count = 0
for i in range(2,len(res)):
    w = real_scale*res[i].height
    h = real_scale*res[i].width
    print(count)
    print((z-x)*(z-y))
    if i % 2 == 0 and count < (z-x)*(z-y):
        dr.rectangle(((up_start[0], up_start[1]),(up_start[0]+ (w if w > h else h), up_start[1]+ (h if w > h else w))),  outline='white')
        if (1 + up_start[0] + (w if w > h else h)) < (scale-draw_x):
            up_start = (up_start[0] + (w if w > h else h), up_start[1] + 0)
        else:
            up_start = (up_start[0], up_start[1] + (h if w > h else w))
        count += res[i].width*res[i].height
    else:
        dr.rectangle(((down_start[0],down_start[1]),(down_start[0] + (h if w > h else w), down_start[1] +  (w if w > h else h))), outline='white')
        if (1 + down_start[1] + (w if w > h else h)) < (scale):
           down_start = (down_start[0], down_start[1] + (w if w > h else h))
        else:
           down_start = (down_start[0] + (h if w > h else w), down_start[1])
    if (-1 + square_start[1] + (h if w > h else w)) > (draw_x):
        square_start = old
    elif (1 + square_start[1] + (h if w > h else w)) > (draw_x):
        old = (square_start[0]+res[i-1].width*real_scale, square_start[1]-res[i-1].height*real_scale)

    dr.rectangle(((square_start[0],square_start[1]),(square_start[0]+ (w if w > h else h), square_start[1]+ (h if w > h else w))), outline='white')

    if (1 + square_start[0] + w if w > h else h) < (draw_y):
        square_start = (square_start[0], square_start[1]+ w if w < h else h)
    else:
        square_start = (square_start[0], square_start[1] + h if w > h else w)

dr.text((30,750), str(x)+"^2 + " +str(y) + "^2 = "+str(z)+"^2", font=fnt, fill=(255,255,255,128))
dr.text((30,850), "pieces: "+str(len(res)), font=fnt, fill=(255,255,255,128))


dr.rectangle(((0,scale),(draw_y,scale-draw_y)), outline='black')
dr.rectangle(((scale-draw_x,0),(scale,draw_x)), outline='yellow')
dr.rectangle(((0,0),(scale,scale)), outline='black')

im.save(str(x)+"_"+str(y)+"_"+str(z)+"_triple.png")
