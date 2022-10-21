
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1231"
    oDesc = "STAN"
    oIndex = "0C"
    hexID = "PRPR1231"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev C')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_ADXL345_PCB')
    newPart['gitName'].append('Adafruit_ADXL345_PCB')
    newPart['eagleBoard'].append('ADXL345 STEMMA QT.brd')
    newPart['eagleSchem'].append('ADXL345 STEMMA QT.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

