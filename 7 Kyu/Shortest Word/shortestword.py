def find_short(s):
    s = s.split(" ")
    returnString = s[0]
    for i in range(len(s)):
        if len(s[i]) <= len(returnString):
            returnString = s[i]
    return len(returnString) # l: shortest word length