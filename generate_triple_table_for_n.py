from __future__ import print_function
import math
import argparse
import fractions
import math
import matplotlib.pyplot as plt
import pytablewriter
from triple_calcs import calc, Triple
from mpl_toolkits.mplot3d import Axes3D


def pythagorean_triple(s, t):
    a = s**2-t**2
    b = 2*s*t
    c = s**2+t**2
    return (a, b, c)

def s_t_generator(upper_bound):
    limit = upper_bound + 1
    for t in range(limit-2, limit-1):
        for s in range(t + 1, limit+1000):
            # Check if s & t are coprime
            if fractions.gcd(s, t) != 1:
                continue
            if s%2 == 1 and t%2 == 1:
                continue
            yield (s, t)

parser = argparse.ArgumentParser(description='Calculate minimal partition for pythagorean triple')
parser.add_argument('x', metavar='x', type=int, nargs='+',
                                   help='limit')

args = parser.parse_args()

limit = vars(args).get('x')[0]
count = 0
triples = []
tuple_result = []
writer = pytablewriter.MarkdownTableWriter()
n = limit
writer.table_name = "n="+str(n)
writer.header_list = ["n", "m", "triple", "z-y", "x%(z-y)","partition size", "x-z+y", "(z-x)%(x-z+y)"]
writer.value_matrix = []
threshold = False
for s, t in s_t_generator(n+1):
    #print(str(s)+", " + str(t) + ": ", end='')
    triple = pythagorean_triple(s, t)
    triple = Triple(triple[0] if triple[0]<triple[1] else triple[1], triple[1] if triple[0]<triple[1] else triple[0], triple[2])
    if triple.y + 1 == triple.z:
        pass
    if triple.y + 2 == triple.z:
        pass
    if 2*s*t < pow(s,2)-pow(t,2) and not threshold:
        threshold = True
        writer.value_matrix.append(['THRESHOLD'])

    count +=1
    writer.value_matrix.append([t, s, str(triple), triple.z-triple.y, triple.x%(triple.z-triple.y), len(calc(triple)), triple.x-triple.z+triple.y, (triple.z-triple.x)%(triple.x-triple.z+triple.y)])
    tuple_result.append((triple.x, triple.y, triple.z, len(calc(triple)), triple.z-triple.y, float(100/(triple.x%(triple.z-triple.y))) if triple.x%(triple.z-triple.y) != 0 else 0, t))
    #print()
    #print()
    #print(str(s)+":"+str(t)+ " - " + str(triple) +": " + str(len(calc(triple))))
    #print((triple.x%(triple.z-triple.y)) if triple.x%(triple.z-triple.y) != 0 else 0)
    #print((triple.z-triple.x)%(triple.x-triple.z+triple.y)*2 > triple.x-triple.z+triple.y)
    #print(triple.x-triple.z+triple.y)
    #print((triple.z-triple.x)%(triple.x-triple.z+triple.y))

tuple_result = sorted(tuple_result, key=lambda x: x[0])

plt.scatter([x[0] for x in tuple_result], [x[3] for x in tuple_result], label='partition size')
plt.legend()
plt.xlabel('x')
#plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax2 = fig.gca(projection='3d')
ax.scatter([x[0] for x in tuple_result], [x[6] for x in tuple_result], [x[3] for x in tuple_result], label='partition size')
ax.scatter([x[0] for x in tuple_result], [x[6] for x in tuple_result], [x[5] for x in tuple_result], label='100/x%(z-y)')
ax.legend()
ax.set_xlabel('x value of x^2+y^2=z^2 with x < y')
ax.set_ylabel('n value of euklids formula')
ax.set_zlabel('minimal partition size')
plt.title('minimal partition size for increasing x with n=5')
#plt.show()


writer.write_table()
