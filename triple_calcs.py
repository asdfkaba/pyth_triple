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
            tmp+=rect.width*rect.height
    return val==tmp

def build_split_up(rest_of_c, rest_of_d):
    solution = []
    x,y = rest_of_d.width, rest_of_d.height
    second = rest_of_c
    while(not is_finished(solution, x*y)):
        if rest_of_c.width<rest_of_d.width and second.width<rest_of_d.width:
            candidate_width= rest_of_c.width
            second_width= second.width
            if rest_of_c.height + second.height < rest_of_d.height:
                candidate_height = rest_of_c.height
                second_height = second.height
                rest_of_d= Rect('dummy', rest_of_d.width, rest_of_d.height-rest_of_c.height)
            elif rest_of_c.height > rest_of_d.height:
                candidate_height = rest_of_d.height
                second_height = rest_of_d.height
                rest_of_d= Rect('dummy', rest_of_d.width-candidate_width-second_width, rest_of_d.height)
            else:
                candidate_height = rest_of_c.height
                second_height = rest_of_d.height-candidate_height
                rest_of_d= Rect('dummy', rest_of_d.width-candidate_width, rest_of_d.height)
            rest_of_c= Rect('dummy', rest_of_c.width, rest_of_c.height-candidate_height)
            second= Rect('dummy', second.width, second.height-second_height)
        else:
            if rest_of_c.height + second.height < rest_of_d.height:
                candidate_height = rest_of_c.height
                second_height = second.height
            else:
                candidate_height = rest_of_c.height
                second_height = rest_of_d.height-candidate_height
            candidate_width = rest_of_d.width
            second_width = rest_of_d.width
            rest_of_d= Rect('', rest_of_d.width, rest_of_d.height-rest_of_c.height-second.height)
            rest_of_c= Rect('', rest_of_c.width-candidate_width, rest_of_c.height)
            second= Rect('', second.width-candidate_width, second.height)
        candidate = Rect('Part from splitted Cs in Picture', candidate_width, candidate_height)
        second_candidate = Rect('Part from splitted Cs in Picture', second_width, second_height)
        if candidate.width > 0 and candidate.height > 0:
            solution.append(candidate)
        if second_candidate.width > 0 and second_candidate.height > 0:
            solution.append(second_candidate)
    return solution

def calc(triple):
    x, y, z = triple.x, triple.y, triple.z
    trip = Triple(x if x < y else y ,y if x < y else x,z)
    res = _calc(trip)
    return res

def _calc(triple):
    solution = []
    solution2 = []
    # append square with area=y^2 (PICTURE: A)
    solution.append(Rect('A in Picture', triple.y, triple.y))
    solution2.append(Rect('A in Picture', triple.y, triple.y))
    # append rect angle form (PICTURE: B)
    solution.append(Rect('B in Picture', triple.x, triple.z-triple.y))
    solution.append(Rect('B in Picture', triple.x, triple.z-triple.y))
    solution2.append(Rect('B in Picture', triple.x, triple.z-triple.y))
    solution2.append(Rect('B in Picture', triple.x, triple.z-triple.y))

    # missing pieces(2 equal forms with width m=z-x and height n=z-y (PICTURE: C)) which we have to split up to fill rest_of_d.size n^2 with n = x-(z-y))
    # together with rect angle form with minimal possible amount of pieces
    c = Rect('dummy', triple.z-triple.y, triple.z-triple.x)
    c2 = Rect('dummy', triple.z-triple.x, triple.z-triple.y)
    d_length = triple.x-(triple.z-triple.y)
    d = Rect('dummy', d_length, d_length)

    # do the minimal split up and append result to solution
    solution += build_split_up(c, d)
    solution2 += build_split_up(c2,d)
    if len(solution2) < len(solution):
        solution = solution2
    return solution
