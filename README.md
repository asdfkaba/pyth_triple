## Table of Contents
- [Intro](#intro)
- [Usage](#usage)
- [Example Pictures](#examples)
- [Theoretical Thoughts](#theoretical-thoughts)


## Intro

gives a splitup of the z^2 area of a pythagorean triple (x,y,z) to build x^2 and y^2 area out of this parts
(maybe minimal under the condition of only using rectangles and no rectilinear polygons)

Primitive pythagoraen triples can be generated with euklids formula

`x = m² - n², y = 2mn, z = m² + n²` with `m, n ∈ ℕ, m > n, gcd(m,n) = 1, ¬(odd(m) & odd(n))`

The algorithm for creating the splitup:
  - ensure x in triple is smaller than y, switch them if not
  - take y^2 out of z^2 (bottom left corner square area(partially hidden) in the [pictures](#examples))
  - Take biggest possible part out of remaining area which can be placed in x^2 (top right corner area in the pictures)
  - Split remaining two rectangles with minimal amount of cuts to fill the missing square area of x^2

An **upper bound** for the splitup size k is for all primitive triples(x,y,z) generated with the above formula:

**`k(m,n) ≤ (2*n+2) + (m-n-1)*1/n`**

Furthermore you have a set of triples whose splitup size is located on this area.

**`k(m,n) = (2*n+2) + (m-n-1)*1/n ∀x.x ∈ { Triple(m, n) | m-n=1+i*2n, i ∈ ℕ }`**

This includes for example all triples generated with `n=1`

The triples ∉ `{ Triple(m, n) | m-n=1+i*2n, i ∈ ℕ }`, which is by far the majority, have a way lower splitup size, especially for big triples, which you can see [here](examples/stats5.png).

## Usage

- pyth_triple.py
  - generates a splitup for the given triple(x,y,z) and draws a split up picture to x_y_z_triple.png
  - usage `python pyth_triple.py x y z`
- generate_triple_table_for_n.py
  - generates a markdown table for given n and optional limit(default=1000)(from n=n, m=n+1 until n=n, m=n+limit
  - usage `python generate_triple_table_for_n.py n [--limit limit]` 
e.g. `python generate_triple_table_for_n.py 1 --limit 1000` creates 
this [output](results/01.md)
# Examples

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/20_21_29_triple.png" width="400" hspace="20"><img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/39_80_89_triple.png" width="400" hspace="20">

## Theoretical thoughts

Primitive pythagoraen triples can be generated with euklids formula

`x = m² - n², y = 2mn, z = m² + n²` with `m, n ∈ ℕ, m > n, gcd(m,n) = 1, ¬(odd(m) & odd(n))`

You can see, for increasing n values the partition size increases slower for bigger x values.
<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats1.png" width="800">


You can see there exists a simple formula for two classes of pythagorean triples to calculate the partition size(k):
 - `k = x+1` if `z-y = 1 (z-y = 1 ⇔ m-n = 1)` (always the first entry in [results](results)/*.md)
 - `k = x/2 + 2` if `z-y = 2 (z-y = 2 ⇔ n = 1 ∧ m > 2)` (see [results/01.md](results/01.md))

### n=5

If you look at one specific n value, for example `n=5`, you see the generated pythagorean triples all have distance `c(z, y) = 2n²` after threshold `2mn < m²-n²` (before: `c(z,y) = (m-n)²`).

`c(z,y) ∈ { 2n² | n ∈ ℕ } ∪ { n² | n ∈ ℕ, n%2 != 0 }`

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats2.png" width="800">

The trend is linear if you only look at every 4th point. Between two of these points there is always the same sequence, which depends on the r emainder of `x/(z-y)`. If the remainder is smaller you need more parts to fillup the area `x*remainder`

The distance Δm between two peak points is for all n: `Δm(peak1, peak2) = 2*n`
The difference in partiton size Δk between two peak points for all n is: `Δk(peak1, peak2)=2`
The first peak is always `k(peak1) = 2*n+2` and it always occurs at `m=n+1`

Combining those leads to the conclusion that for a given n the partition size for all peak points is: 

`k(peak.m, n) = (2*n+2) + (m-n-1)*1/n` (1)

in the picture above you have for example the peaks: `k(16) = 14`, `k(26) = 16`, `k(36) = 18` and `k(46) = 20`

for [n=37](results/37.md) you have: `k(112) = 78`, `k(186) = 80`, `k(260) = 82` and `k(334) = 84`

**The formula above (1) is also an upper bound for all pythagorean triples (x, y, z):**

`k(m,n) ≤ (2*n+2) + (m-n-1)*1/n`

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats4.png" width="800">

in the next picture you can see the local peaks apear when the remainder is minimal and 100/remainder is maximal.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/stats3.png" width="800">



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

### n=6
If you look at the table for `n=6`, you see another influence on the partition size.


|n | m  | triple           | x%(z-y)       | partition size  | x-z+y | (z-x)%(x-z+y) |
|- |--- |----------------- |:-------------:| :--------------:|:-----:|:-------------:|
|6 | 17 | (204, 253, 325)  | 60            | 10              | 132   | 121           |
|6 | 19 | (228, 325, 397)  | **12**        | **16**          | 156   | 13            |
|6 | 23 | (276, 493, 565)  | 60            | 12              | 204   | 85            |
|6 | 25 | (300, 589, 661)  | **12**        | **11**          | 228   | 133           |
|6 | 29 | (348, 805, 877)  | 60            | 12              | 276   | 253           |
|6 | 31 | (372, 925, 997)  | 12            | 18              | 300   | 25            |

`x-z-y` is the size of the square we want fo fill.
`(z-x)%(x-z+y)` is the remainder of the split up rectangles, which is coloured pink in the right picture.

The partition size is for `m=19` with 16 way higher than for `m=25`, even for both `x%(y-z)=12`.
The difference you can see in the following pictures.

<img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/228_325_397_triple.png" width="400" hspace="20"><img src="https://raw.githubusercontent.com/asdfkaba/pyth_triple/master/examples/300_589_661_triple.png" width="400" hspace="20">

One the left site there is only `(z-x)%(x-z+y)=13` to fill the missing area, so you end up with many little pieces.
One the right site first of all much more space is left and additionally `(z-x)%(x-z+y)=133` doesn't fit twice into `x-z+y=228`, which allows you to choose a little more efficient way. You could have choosen to place two 114-width pieces and end up at 12 pieces instead.

you can find more result tables for n ∈ {1,2,...,40} under [results](results)
