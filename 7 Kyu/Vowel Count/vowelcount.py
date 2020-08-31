import re
def get_count(input_str):
    x = re.findall("[aeiou]",input_str)
    return len(x)
    