
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4438"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4438"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DSOX PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DSOX-PCB')
    newPart['gitName'].append('Adafruit-LSM6DSOX-PCB')
    newPart['eagleBoard'].append('/Adafruit_LSM6DSOX.brd')
    newPart['eagleSchem'].append('/Adafruit_LSM6DSOX.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

