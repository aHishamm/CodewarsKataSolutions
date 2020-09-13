import re 
def find_nth_occurrence(substring, string, occurrence=1):
    start = string.find(substring)
    while start >= 0 and occurrence > 1: 
        start = string.find(substring,start+1)
        occurrence -= 1 
    return start

