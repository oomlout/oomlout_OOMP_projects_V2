
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4888"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4888"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ItsyBitsy RP2040 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ItsyBitsy-RP2040-PCB')
    newPart['gitName'].append('Adafruit-ItsyBitsy-RP2040-PCB')
    newPart['eagleBoard'].append('/Adafruit ItsyBitsy RP2040.brd')
    newPart['eagleSchem'].append('/Adafruit ItsyBitsy RP2040.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

