
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2107"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2107"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit USB Isolator PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-USB-Isolator-PCB')
    newPart['gitName'].append('Adafruit-USB-Isolator-PCB')
    newPart['eagleBoard'].append('/Adafruit USB Isolator.brd')
    newPart['eagleSchem'].append('/Adafruit USB Isolator.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

