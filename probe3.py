def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    res = []
    while lng != wdth:
        var = lng - wdth
        res.append(wdth)
        lng = var
        if lng < wdth:
            lng, wdth = wdth, lng
    res.append(wdth)
    return res

print(sqInRect(5, 5))