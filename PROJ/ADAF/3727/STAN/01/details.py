
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3727"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3727"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ItsyBitsy M0 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ItsyBitsy-M0-PCB')
    newPart['gitName'].append('Adafruit-ItsyBitsy-M0-PCB')
    newPart['eagleBoard'].append('/Adafruit ItsyBitsy M0.brd')
    newPart['eagleSchem'].append('/Adafruit ItsyBitsy M0.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

