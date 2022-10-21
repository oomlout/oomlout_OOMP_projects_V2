
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "1918"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR1918"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit GUVA Analog UV Sensor Breakout PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-GUVA-Analog-UV-Sensor-Breakout-PCB')
    newPart['gitName'].append('Adafruit-GUVA-Analog-UV-Sensor-Breakout-PCB')
    newPart['eagleBoard'].append('/Adafruit GUVA UV Sensor Breakout.brd')
    newPart['eagleSchem'].append('/Adafruit GUVA UV Sensor Breakout.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

