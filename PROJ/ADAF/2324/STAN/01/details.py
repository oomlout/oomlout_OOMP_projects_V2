
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2324"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2324"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Ultimate GPS HAT PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Ultimate-GPS-HAT-PCB')
    newPart['gitName'].append('Adafruit-Ultimate-GPS-HAT-PCB')
    newPart['eagleBoard'].append('/Adafruit Ultimate GPS HAT.brd')
    newPart['eagleSchem'].append('/Adafruit Ultimate GPS HAT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

