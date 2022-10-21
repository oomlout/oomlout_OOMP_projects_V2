
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2809"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2809"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LIS3DH Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LIS3DH-Breakout-PCB')
    newPart['gitName'].append('Adafruit-LIS3DH-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit LIS3DH Original.brd')
    newPart['eagleSchem'].append('/Adafruit LIS3DH Original.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

