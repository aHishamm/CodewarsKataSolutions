import re
def song_decoder(song):
    x = re.sub('(WUB)+',' ',song).strip()
    print(x)
    return x