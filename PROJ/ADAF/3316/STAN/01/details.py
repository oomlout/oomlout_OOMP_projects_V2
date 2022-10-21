
######  Auto translated oomp file

def load(newPart):
    oType = "PROJ"
    oSize = "ADAF"
    oColor = "3316"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "PRPR3316"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('Adafruit VL6180X ToF Distance Sensor PCB')
    newPart['gitRepo'].append('https://github.com/adafruit/Adafruit-VL6180X-ToF-Distance-Sensor-PCB')
    newPart['gitName'].append('Adafruit-VL6180X-ToF-Distance-Sensor-PCB')
    newPart['eagleBoard'].append('/Adafruit VL6180 Time of Flight Sensor.brd')
    newPart['eagleSchem'].append('/Adafruit VL6180 Time of Flight Sensor.sch')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

