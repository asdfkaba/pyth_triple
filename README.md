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

If you look at one specific n value, for example n = 5, you see the generated pythagorean triples all have distance `c(z, y) = 2n²` after threshold `2mn = m²-n²`.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats2.png" width="800">

The trend is linear if you only look at every 4th point. Between 5 dots there is always the same sequence, which depends on the remainder of `x/(z-y)`.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats3.png" width="800">

 m  | triple           | x%(y-z)       | partition size  |
--- | ---------------- |:-------------:| :--------------:|
 14 | (140, 171, 221)  | 40            | 9               |
 16 | (160, 231, 281)  | 10            | 14              |
 18 | (180, 299, 349)  | 30            | 10              |
 22 | (220, 459, 509)  | 20            | 10              |
 24 | (240, 551, 601)  | 40            | 11              |
 26 | (260, 651, 701)  | 10            | 16              |
