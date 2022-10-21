
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1231"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1231"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ADXL345 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit_ADXL345_PCB')
    newPart['gitName'].append('Adafruit_ADXL345_PCB')
    newPart['eagleBoard'].append('/Adafruit ADXL345 Triple-Axis Accelerometer.brd')
    newPart['eagleSchem'].append('/Adafruit ADXL345 Triple-Axis Accelerometer.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

