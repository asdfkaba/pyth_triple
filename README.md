gives a splitup of the z^2 area of a pythagorean triple (x,y,z) to build x^2 and y^2 area out of this parts
(maybe minimal under the condition of only using rectangles and no rectilinear polygons)

usage `python pyth_triple.py x y z`

requirements:
 - PIL


exmaples:

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/20_21_29_triple.png" width="400" hspace="20"><img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/39_80_89_triple.png" width="400" hspace="20">

Primitive pythagoraen triples can be generated with euklids formula
`x = m² - n², y = 2mn, z = m² + n²` with `m, n ∈ ℕ, m > n, gcd(m,n) = 1, ¬(odd(m) & odd(n)`

You can see, for increasing n values the partition size increases slower for bigger x values.
<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats1.png" width="800">

If you look at one specific n value, for example `n=5`, you see the generated pythagorean triples all have distance `c(z, y) = 2n²` after threshold `2mn < m²-n²`.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats2.png" width="800">

The trend is linear if you only look at every 4th point. Between 5 dots there is always the same sequence, which depends on the remainder of `x/(z-y)`. If the remainder is smaller you need more parts to fillup the area `x*remainer`

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats3.png" width="800">

you can see the local peaks apear when the remainder is minimal and 100/remainder is maximal.


|n | m  | triple           | x%(z-y)       | partition size  |
|- |--- |----------------- |:-------------:| :--------------:|
|5 | 6  | (11, 60, 61)     | 0             | 12              |
|5 | 8  | (39, 80, 89)     | 3             | 8               |
|5 | 12 | (119, 120, 169   | 21            | 8               |
|  |    |   THRESHOLD      |               |                 |
|5 | 14 | (140, 171, 221)  | 40            | 9               |
|5 | 16 | (160, 231, 281)  | 10            | 14              |
|5 | 18 | (180, 299, 349)  | 30            | 10              |
|5 | 22 | (220, 459, 509)  | 20            | 10              |
|5 | 24 | (240, 551, 601)  | 40            | 11              |
|5 | 26 | (260, 651, 701)  | 10            | 16              |


If you look at the table for `n=6`, you see another influence on the partition size.


|n | m  | triple           | x%(z-y)       | partition size  |
|- |--- |----------------- |:-------------:| :--------------:|
|6 | 17 | (204, 253, 325)  | 60            | 10              |
|6 | 19 | (228, 325, 397)  | 12            | 16              |
|6 | 23 | (276, 493, 565)  | 60            | 12              |
|6 | 25 | (300, 589, 661)  | 12            | 11              |
|6 | 29 | (348, 805, 877)  | 60            | 12              |
|6 | 31 | (372, 925, 997)  | 12            | 18              |

The partition size is for m=25 with 11 smaller than for m=23, even there is only 12 height left.
The difference you can see in the following pictures.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/276_493_565_triple.png" width="300" hspace="20"><img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/300_589_661_triple.png" width="300" hspace="20">

if you would've added a piece with same height as the pink one from bottom right corner(the light green in this picture), you would have ended with 12 pieces.

