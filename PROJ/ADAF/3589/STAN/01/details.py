
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3589"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3589"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit PiUART PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-PiUART-PCB')
    newPart['gitName'].append('Adafruit-PiUART-PCB')
    newPart['eagleBoard'].append('/Adafruit PiUART USB C.brd')
    newPart['eagleSchem'].append('/Adafruit PiUART USB C.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

