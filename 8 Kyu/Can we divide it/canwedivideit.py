import math
def is_divide_by(number, a, b):
    if math.modf(abs(number/a))[0] != 0.0 or math.modf(abs(number/b))[0] != 0.0: 
        return False
    return True