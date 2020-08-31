import re
def is_letter(s):
    if len(s) != 1: return False
    s = re.findall("[a-z]|[A-Z]", s)
    if s: return True
    else: return False