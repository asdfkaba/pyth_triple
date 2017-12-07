import math
import argparse
import fractions
import math
from triple_calcs import calc, Triple

def pythagorean_triple(s, t):
    a = s**2-t**2
    b = 2*s*t
    c = s**2+t**2
    return (a, b, c)

def s_t_generator(upper_bound):
    limit = upper_bound + 1
    for t in range(1, limit-1):
        for s in range(t + 1, limit):
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
for s, t in s_t_generator(100):
    print(str(s)+", " + str(t) + ": ", end='')
    triple = pythagorean_triple(s, t)
    triple = Triple(triple[0], triple[1], triple[2])
    if triple.y + 1 == triple.z:
        pass
    if triple.y + 2 == triple.z:
        pass
    count +=1
    if count > limit:
        break
    calc(triple)
    print(str(triple) +": " + str(len(calc(triple))))

triples = sorted(triples, key=lambda triple: triple[2])
# print(len(triples))
for triple in triples:
    triple = Triple(triple[0] if triple[0] < triple[1] else triple[1], triple[1] if triple[0] < triple[1] else triple[0], triple[2])
    print(str(triple) +": " + str(len(calc(triple))))
