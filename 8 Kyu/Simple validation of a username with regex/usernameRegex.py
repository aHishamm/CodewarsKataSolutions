import re
def validate_usr(username):
    x = re.match('^[a-z0-9_]{4,16}$', username)
    if x: 
        return True
    return False