from __future__ import print_function
from __future__ import division
import math
import random
import argparse
import fractions
import math
import matplotlib.pyplot as plt
import pytablewriter
from triple_calcs import calc, Triple
from draw_triple_picture import draw
from mpl_toolkits.mplot3d import Axes3D

upper_limit = 1000

def pythagorean_triple(s, t):
    a = s**2-t**2
    b = 2*s*t
    c = s**2+t**2
    return (a, b, c)

def upper_bound(s, t):
    return (2*t+2) + (s-t-1)*1/t

def s_t_generator(upper_bound):
    limit = upper_bound + 1
    for t in range(limit-2, limit-1):
        for s in range(t + 1, limit+upper_limit):
            # Check if s & t are coprime
            if fractions.gcd(s, t) != 1:
                continue
            if s%2 == 1 and t%2 == 1:
                continue
            if 2*s*t > pow(s,2)-pow(t,2):
                pass
            yield (s, t)

parser = argparse.ArgumentParser(description='Calculate minimal partition for pythagorean triple')
parser.add_argument('x', metavar='n', type=int, nargs='+',
                                   help='limit')
parser.add_argument('--limit', metavar='limit', type=int,
                    default=upper_limit, help='limit')

args = parser.parse_args()

n = vars(args).get('x')[0]
upper_limit = vars(args).get('limit')-1

count = 0
triples = []
tuple_result = []
writer = pytablewriter.MarkdownTableWriter()
writer.table_name = "n="+str(n)
writer.header_list = ["n", "m", "triple", "z-y", "x%(z-y)","partition size", "upper bound", "x-z+y", "(z-x)%(x-z+y)"]
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

    x,y,z = triple.x, triple.y, triple.z
    count +=1
    sol = calc(triple)

    ## draw random some splitup pictures
    if random.randint(0,29) == 22 and ((t < 3 and z < 1000 and z-y > 1) or (z < 1000 and z-y > 5) or (z < 10000 and z-y > 30)):
        draw(1000, sol, triple.x, triple.y, triple.z)


    writer.value_matrix.append([t, s, str(triple), triple.z-triple.y, triple.x%(triple.z-triple.y), len(sol), upper_bound(s,t), triple.x-triple.z+triple.y, (triple.z-triple.x)%(triple.x-triple.z+triple.y)])

    tuple_result.append((triple.x, triple.y, triple.z, len(sol), triple.z-triple.y,
                         float(100/(triple.x%(triple.z-triple.y))) if triple.x%(triple.z-triple.y) != 0 else 0, t, s,
                         float((triple.z-triple.x)%(triple.x-triple.z+triple.y))
                        ))

tuple_result = sorted(tuple_result, key=lambda x: x[0])

# plt.scatter([x[7] for x in tuple_result], [x[3] for x in tuple_result], label='partition size k for n='+str(n))
# plt.plot([x[7] for x in tuple_result], [upper_bound(x[7], x[6]) for x in tuple_result], label='upper bound for k: k(m,n) <= (2*n+2) + (m-n-1)*1/n', color='orangered')

plt.scatter([x[7] for x in tuple_result], [x[3] for x in tuple_result], label='partition size k for n='+str(n))
plt.scatter([x[7] for x in tuple_result], [x[5] for x in tuple_result], label='100/x%(z.y)')
plt.scatter([x[7] for x in tuple_result], [100/x[8] if x[8] != 0 else 0 for x in tuple_result], label='(z-x)%(x-z+y)')

plt.legend()
plt.xlabel('m')
##2D Plot (x,partition size)
#plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax2 = fig.gca(projection='3d')
ax.scatter([x[7] for x in tuple_result], [x[6] for x in tuple_result], [x[3] for x in tuple_result], label='partition size for n='+str(n))
#  ax.scatter([x[7] for x in tuple_result], [x[6] for x in tuple_result], [x[5] for x in tuple_result], label='100/x%(z-y)')
ax.legend()
ax.set_xlabel('m value of euklids formula')
ax.set_ylabel('n value of euklids formula')
ax.set_zlabel('minimal partition size')
plt.title('minimal partition size for increasing x with n='+str(n))
## 3D Plot(x, n, partition size) & (x, n, 100/x%(z-y))
#plt.show()


writer.write_table()
