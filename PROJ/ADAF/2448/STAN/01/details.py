
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "2448"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR2448"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit TB6612 Motor Driver Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-TB6612-Motor-Driver-Breakout-PCB')
    newPart['gitName'].append('Adafruit-TB6612-Motor-Driver-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit TB6612.brd')
    newPart['eagleSchem'].append('/Adafruit TB6612.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

