
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "5591"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR5591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LTR 329 LTR 303 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LTR-329-LTR-303-PCB')
    newPart['gitName'].append('Adafruit-LTR-329-LTR-303-PCB')
    newPart['eagleBoard'].append('/Adafruit LTR-303.brd')
    newPart['eagleSchem'].append('/Adafruit LTR-303.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

