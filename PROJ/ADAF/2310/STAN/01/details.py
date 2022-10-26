
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2310"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2310"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Perma Proto HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Perma-Proto-HAT-PCB')
    newPart['gitName'].append('Adafruit-Perma-Proto-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit HaD Proto HAT rev A.brd')
    newPart['eagleSchem'].append('/Adafruit HaD Proto HAT rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

