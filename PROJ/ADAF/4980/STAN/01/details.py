
######  Auto translated oomp file

def load(newPart,it):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4980"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4980"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit NeoKey 1x4 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-NeoKey-1x4-PCB')
    newPart['gitName'].append('Adafruit-NeoKey-1x4-PCB')
    newPart['eagleBoard'].append('/Adafruit NeoKey 1x4 QT I2C.brd')
    newPart['eagleSchem'].append('/Adafruit NeoKey 1x4 QT I2C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

