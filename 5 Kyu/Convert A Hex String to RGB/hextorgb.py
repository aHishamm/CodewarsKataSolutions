def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.lower()
    rVal = hex_string[1:3] ; rint = int(rVal,16)
    gVal = hex_string[3:5] ; gint = int(gVal,16)
    bVal = hex_string[5:7] ; bint = int(bVal,16)
    return {'r': rint, 'g': gint, 'b': bint}