import re
def validate_code(code):
    x = re.findall("^1|^2|^3", str(code))
    if x: return True 
    return False