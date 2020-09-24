def maskify(cc):
    cc = list(cc)
    if len(cc) <= 4: 
        return "".join(cc)
    else: 
        for i in range(len(cc)-4):
            cc[i] = '#'
        return "".join(cc)