
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3387"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3387"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM9DS1 Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM9DS1-Breakout-PCB')
    newPart['gitName'].append('Adafruit-LSM9DS1-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit LSM9DS1 Rev A.brd')
    newPart['eagleSchem'].append('/Adafruit LSM9DS1 Rev A.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

