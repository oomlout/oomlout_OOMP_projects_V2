
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3800"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3800"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ItsyBitsy M4 Express PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ItsyBitsy-M4-Express-PCB')
    newPart['gitName'].append('Adafruit-ItsyBitsy-M4-Express-PCB')
    newPart['eagleBoard'].append('/Adafruit ItsyBitsy M4.brd')
    newPart['eagleSchem'].append('/Adafruit ItsyBitsy M4.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

