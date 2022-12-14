
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1135"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1135"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Perma Proto Pi PCBs')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Perma-Proto-Pi-PCBs')
    newPart['gitName'].append('Adafruit-Perma-Proto-Pi-PCBs')
    newPart['eagleBoard'].append('/Adafruit Perma Proto Pi - Full Size.brd')
    newPart['eagleSchem'].append('/Adafruit Perma Proto Pi - Full Size.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

