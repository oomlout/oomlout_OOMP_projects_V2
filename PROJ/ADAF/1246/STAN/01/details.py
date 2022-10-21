
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1246"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1246"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit Flora TSL2561 Lux Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-Flora-TSL2561-Lux-Sensor-PCB')
    newPart['gitName'].append('Adafruit-Flora-TSL2561-Lux-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit Flora TSL2561 Lux.brd')
    newPart['eagleSchem'].append('/Adafruit Flora TSL2561 Lux.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

