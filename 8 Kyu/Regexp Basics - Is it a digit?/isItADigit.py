import re
def is_digit(n):
    z = re.findall("\A\d\Z",n)
    if z: return True
    return False