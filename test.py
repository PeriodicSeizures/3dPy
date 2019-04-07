class t:
    def __init__(self, f):
        self.f = [i for i in f]

var = [1,2,3]

test = t(var)

print(test.f)

var[1] = 9

print(test.f)
