
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4503"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4503"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit LSM6DS3TR C PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-LSM6DS3TR-C-PCB')
    newPart['gitName'].append('Adafruit-LSM6DS3TR-C-PCB')
    newPart['eagleBoard'].append('/Adafruit_LSM6DS3.brd')
    newPart['eagleSchem'].append('/Adafruit_LSM6DS3.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

