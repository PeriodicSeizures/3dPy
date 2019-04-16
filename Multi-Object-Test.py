class apple:
    def __init__(self):
        pass

class banana:
    def __init__(self):
        pass

fruits = [apple(), banana()]

if isinstance(fruits[0], apple):
    print("Is a apple")
