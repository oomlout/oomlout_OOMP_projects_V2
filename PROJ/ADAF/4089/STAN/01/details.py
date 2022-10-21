
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "4089"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR4089"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit ADT7410 PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-ADT7410-PCB')
    newPart['gitName'].append('Adafruit-ADT7410-PCB')
    newPart['eagleBoard'].append('/Adafruit ADT7410 I2C Temperature Sensor.brd')
    newPart['eagleSchem'].append('/Adafruit ADT7410 I2C Temperature Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

