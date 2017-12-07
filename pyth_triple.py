from __future__ import print_function
from __future__ import division
import argparse
import sys
import itertools
from draw_triple_picture import draw
from triple_calcs import Triple, calc


parser = argparse.ArgumentParser(description='Calculate minimal partition for pythagorean triple')
parser.add_argument('x', metavar='x', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')
parser.add_argument('y', metavar='y', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')
parser.add_argument('z', metavar='z', type=int, nargs='+',
                                   help='x^2 + y^2 = z^2')

args = parser.parse_args()

x,y,z = vars(args).get('x')[0], vars(args).get('y')[0], vars(args).get('z')[0]
if pow(x,2) + pow(y,2) != pow(z, 2):
    print("x,y,z is not a pythagorean triple")
    sys.exit(0)
trip = Triple(x if x < y else y ,y if x < y else x,z)
res = calc(trip)
trip2 = Triple(x if x > y else y ,y if x> y else x,z)
res2 = calc(trip2)
print(len(res))
print(len(res2))
if len(res2) < len(res):
    print("FOUNDONE: " + str(trip2))
    res = res2


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
print("Result Parts:")

for re in res:
    print(str(re))

draw(2500, res, x, y, z)
